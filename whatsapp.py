import socket
import threading
import time
import os
import datetime

HOST = "127.0.0.1"
PUERTO_ENVIOS = 666
PUERTO_RECEPCION = 999
SEP = ";"
TIMEOUT = 10

ESTADO_ENVIADO = "ENVIADO"
ESTADO_RECIBIDO = "RECIBIDO"
ESTADO_ENTREGADO = "ENTREGADO"
ESTADO_LEIDO = "LEIDO"
ESTADO_UPDATE = "UPDATE"
ESTADO_LIST = "LIST"

file_mutex = threading.Lock()
local_mutex = threading.Lock()


def begins(texto, pref):
    if texto is None or pref is None:
        return False
    return str(texto)[:len(str(pref))] == str(pref)


def get_timestamp():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def safe_text(texto):
    if texto is None:
        return ""
    return str(texto).replace('"', "'").replace(";", ",").replace("\n", " ")


def msg_create(origen, destino, timestamp, estado, tiempo_estado, texto):
    return {
        "origen": origen,
        "destino": destino,
        "timestamp": timestamp,
        "estado": estado,
        "tiempo_estado": tiempo_estado,
        "texto": texto,
    }


def msg_to_string(m):
    txt_safe = safe_text(m.get("texto", ""))
    return (
        str(m.get("origen", ""))
        + SEP + str(m.get("destino", ""))
        + SEP + str(m.get("timestamp", ""))
        + SEP + str(m.get("estado", ""))
        + SEP + str(m.get("tiempo_estado", ""))
        + SEP + '"' + txt_safe + '"'
    )


def msg_from_string(cadena):
    try:
        if cadena is None:
            return None
        cad = cadena.strip()
        if cad == "":
            return None
        partes = cad.split(SEP)
        if len(partes) < 6:
            return None
        texto_limpio = SEP.join(partes[5:]).replace('"', "")
        return msg_create(partes[0], partes[1], partes[2], partes[3], partes[4], texto_limpio)
    except Exception:
        return None


def file_read_lines(path_):
    lines = []
    f = None
    try:
        f = open(path_, "r", encoding="utf-8")
        line = f.readline()
        while line != "":
            lines.append(line)
            line = f.readline()
    except Exception:
        lines = []
    finally:
        if f:
            f.close()
    return lines


def file_write_lines(path_, lines):
    f = None
    try:
        f = open(path_, "w", encoding="utf-8")
        i = 0
        while i < len(lines):
            f.write(lines[i])
            i += 1
    finally:
        if f:
            f.close()


def file_append_line(path_, line):
    f = None
    try:
        f = open(path_, "a", encoding="utf-8")
        f.write(line)
    finally:
        if f:
            f.close()


def generar_usuarios_si_no_existen():
    if not os.path.exists("usuarios.txt"):
        file_append_line(
            "usuarios.txt",
            "Alfonso:1234\nManuel:1234\nMaria:1234\nPepe:1234\nAdmin:admin\n"
        )


def s_verificar_usuario(login_str):
    try:
        if login_str is None:
            return None
        if not begins(login_str, "LOGIN:"):
            return None
        parts = login_str.strip().split(":")
        if len(parts) != 3:
            return None
        user = parts[1]
        pwd = parts[2]

        if not os.path.exists("usuarios.txt"):
            return None

        lines = file_read_lines("usuarios.txt")
        i = 0
        while i < len(lines):
            p = lines[i].strip().split(":")
            if len(p) == 2:
                u = p[0]
                clave = p[1]
                if u.lower() == user.lower() and clave == pwd:
                    return u
            i += 1
        return None
    except Exception:
        return None


def s_get_archivo_path(u1, u2):
    try:
        files = os.listdir()
    except Exception:
        files = []
    idx = 0
    while idx < len(files):
        fname = files[idx]
        ok_txt = fname[-4:] == ".txt"
        if ok_txt and ("_" in fname) and (not begins(fname, "LOG_")):
            base = fname[:-4]
            parts = base.split("_")
            if len(parts) == 2:
                a = parts[0].lower()
                b = parts[1].lower()
                if (a == u1.lower() and b == u2.lower()) or (a == u2.lower() and b == u1.lower()):
                    return fname
        idx += 1
    return str(u1) + "_" + str(u2) + ".txt"


def s_manejar_envios_666(conn):
    try:
        conn.settimeout(TIMEOUT)
        data = conn.recv(1024).decode(errors="ignore")
        usuario = s_verificar_usuario(data)
        if usuario:
            conn.send(b"OK")
            running = True
            while running:
                raw = conn.recv(4096).decode(errors="ignore")
                if (not raw) or (raw == "FIN"):
                    running = False
                else:
                    msg = msg_from_string(raw)
                    if msg:
                        msg["estado"] = ESTADO_RECIBIDO
                        msg["tiempo_estado"] = get_timestamp()
                        archivo = s_get_archivo_path(msg["origen"], msg["destino"])

                        file_mutex.acquire()
                        try:
                            file_append_line(archivo, msg_to_string(msg) + "\n")
                        finally:
                            file_mutex.release()

                        print("[666] Recibido de " + str(usuario) + " para " + str(msg["destino"]))
                        conn.send(b"OK")
                    else:
                        conn.send(b"KO")
        else:
            conn.send(b"KO")
    except Exception:
        dummy = 0
        dummy += 1
    finally:
        try:
            conn.close()
        except Exception:
            return


def listar_archivos_usuario(usuario):
    try:
        files = os.listdir()
    except Exception:
        files = []
    res = []
    i = 0
    while i < len(files):
        f = files[i]
        ok_txt = f[-4:] == ".txt"
        if ok_txt and (not begins(f, "LOG_")):
            if usuario.lower() in f.lower():
                res.append(f)
        i += 1
    return res


def s_manejar_recepcion_999(conn):
    try:
        conn.settimeout(TIMEOUT)
        data = conn.recv(1024).decode(errors="ignore")
        usuario = s_verificar_usuario(data)

        if usuario:
            conn.send(b"OK")
            raw = conn.recv(4096).decode(errors="ignore")
            cmd = msg_from_string(raw)

            if cmd and cmd.get("estado") == ESTADO_UPDATE:
                conn.send(b"OK")
                msgs_to_send = []
                archivos_validos = listar_archivos_usuario(usuario)

                file_mutex.acquire()
                try:
                    a = 0
                    while a < len(archivos_validos):
                        arch = archivos_validos[a]
                        lines = file_read_lines(arch)
                        updated_lines = []
                        dirty = False

                        j = 0
                        ultimo_ts = cmd.get("texto", "00000000000000")
                        while j < len(lines):
                            m = msg_from_string(lines[j])
                            if m:
                                es_para_mi = (m.get("destino", "").lower() == usuario.lower())
                                es_nuevo = (m.get("estado") == ESTADO_RECIBIDO)
                                es_reciente = (m.get("timestamp", "0") > ultimo_ts)

                                if es_para_mi and es_nuevo and es_reciente:
                                    m["estado"] = ESTADO_ENTREGADO
                                    m["tiempo_estado"] = get_timestamp()
                                    msgs_to_send.append(m)
                                    updated_lines.append(msg_to_string(m) + "\n")
                                    dirty = True
                                else:
                                    updated_lines.append(lines[j])
                            else:
                                updated_lines.append(lines[j])
                            j += 1

                        if dirty:
                            file_write_lines(arch, updated_lines)
                        a += 1
                finally:
                    file_mutex.release()

                header = msg_create(usuario, "@", get_timestamp(), ESTADO_UPDATE, get_timestamp(), str(len(msgs_to_send)))
                conn.send(msg_to_string(header).encode())
                try:
                    conn.recv(1024)
                except Exception:
                    return

                k = 0
                while k < len(msgs_to_send):
                    conn.send(msg_to_string(msgs_to_send[k]).encode())
                    try:
                        conn.recv(1024)
                    except Exception:
                        return
                    k += 1

            elif cmd and cmd.get("estado") == ESTADO_LIST:
                conn.send(b"OK")
                conn.send(msg_to_string(msg_create(usuario, "@", get_timestamp(), ESTADO_LIST, get_timestamp(), "0")).encode())
            else:
                conn.send(b"KO")
        else:
            conn.send(b"KO")
    except Exception:
        dummy = 0
        dummy += 1
    finally:
        try:
            conn.close()
        except Exception:
            return


def s_iniciar_socket(puerto, handler):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((HOST, puerto))
    except Exception:
        return
    s.listen()
    print("Servidor escuchando en " + str(puerto))
    while True:
        c, _ = s.accept()
        threading.Thread(target=handler, args=(c,), daemon=True).start()


def main_servidor():
    generar_usuarios_si_no_existen()
    print("MODO SERVIDOR INICIADO")
    t1 = threading.Thread(target=s_iniciar_socket, args=(PUERTO_ENVIOS, s_manejar_envios_666), daemon=True)
    t2 = threading.Thread(target=s_iniciar_socket, args=(PUERTO_RECEPCION, s_manejar_recepcion_999), daemon=True)
    t1.start()
    t2.start()
    while True:
        time.sleep(1)


C_USUARIO = ""
C_CLAVE = ""
C_CHAT_ACTUAL = None
C_ULTIMO_TS = "00000000000000"
C_RUNNING = True


def c_get_local_file(contacto):
    return "LOG_" + str(C_USUARIO) + "_" + str(contacto) + ".txt"


def c_guardar_local(msg, contacto):
    archivo = c_get_local_file(contacto)
    local_mutex.acquire()
    try:
        file_append_line(archivo, msg_to_string(msg) + "\n")
    finally:
        local_mutex.release()


def c_mostrar_chat(contacto):
    os.system("cls" if os.name == "nt" else "clear")
    print("\n--- CHAT CON @" + str(contacto) + " ---")
    archivo = c_get_local_file(contacto)
    msgs = []

    local_mutex.acquire()
    try:
        if os.path.exists(archivo):
            lines = file_read_lines(archivo)
            i = 0
            while i < len(lines):
                m = msg_from_string(lines[i])
                if m:
                    msgs.append(m)
                i += 1
    finally:
        local_mutex.release()

    msgs.sort(key=lambda x: x.get("timestamp", "0"))

    start = 0
    if len(msgs) > 50:
        start = len(msgs) - 50
    i = start
    while i < len(msgs):
        m = msgs[i]
        pre = ">> Yo" if m.get("origen", "").lower() == C_USUARIO.lower() else "<< " + str(m.get("origen", ""))
        ts = str(m.get("timestamp", ""))
        hhmm = ts[8:12] if len(ts) >= 12 else ts
        print("[" + hhmm + "] " + pre + ": " + str(m.get("texto", "")))
        i += 1

    print("-" * 40)
    print("Escribe mensaje (o @salir, @lista, @Nombre):")
    print("> ", end="", flush=True)


def c_hilo_polling():
    global C_ULTIMO_TS
    while C_RUNNING:
        time.sleep(3)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((HOST, PUERTO_RECEPCION))
            s.send(("LOGIN:" + str(C_USUARIO) + ":" + str(C_CLAVE)).encode())

            if s.recv(1024).decode(errors="ignore") == "OK":
                cmd = msg_create(C_USUARIO, "@", get_timestamp(), ESTADO_UPDATE, get_timestamp(), C_ULTIMO_TS)
                s.send(msg_to_string(cmd).encode())

                if s.recv(1024).decode(errors="ignore") == "OK":
                    head_raw = s.recv(1024).decode(errors="ignore")
                    head = msg_from_string(head_raw)
                    cant = 0
                    if head:
                        t = str(head.get("texto", "0"))
                        if t.isdigit():
                            cant = int(t)
                    s.send(b"OK")

                    nuevos_mensajes = False
                    i = 0
                    while i < cant:
                        raw = s.recv(4096).decode(errors="ignore")
                        m = msg_from_string(raw)
                        if m:
                            c_guardar_local(m, m.get("origen", ""))
                            if m.get("timestamp", "0") > C_ULTIMO_TS:
                                C_ULTIMO_TS = m.get("timestamp", "0")
                            if C_CHAT_ACTUAL and m.get("origen", "").lower() == str(C_CHAT_ACTUAL).lower():
                                nuevos_mensajes = True
                        s.send(b"OK")
                        i += 1

                    if nuevos_mensajes and C_CHAT_ACTUAL:
                        c_mostrar_chat(C_CHAT_ACTUAL)

            try:
                s.close()
            except Exception:
                dummy = 0
                dummy += 1
        except Exception:
            dummy = 0
            dummy += 1


def c_enviar(dest, texto):
    ts = get_timestamp()
    msg = msg_create(C_USUARIO, dest, ts, ESTADO_ENVIADO, ts, texto)
    ok = False
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((HOST, PUERTO_ENVIOS))
        s.send(("LOGIN:" + str(C_USUARIO) + ":" + str(C_CLAVE)).encode())
        if s.recv(1024).decode(errors="ignore") == "OK":
            s.send(msg_to_string(msg).encode())
            if s.recv(1024).decode(errors="ignore") == "OK":
                ok = True
        try:
            s.close()
        except Exception:
            ok = ok
    except Exception:
        ok = False

    if ok:
        c_guardar_local(msg, dest)
        if C_CHAT_ACTUAL and str(C_CHAT_ACTUAL).lower() == str(dest).lower():
            c_mostrar_chat(dest)
    else:
        print("\nSin conexión. Guardando en borrador...")
        file_append_line("LOG_" + str(C_USUARIO) + "_" + str(dest) + "_tmp.txt", msg_to_string(msg) + "\n")


def main_cliente():
    global C_USUARIO, C_CLAVE, C_RUNNING, C_CHAT_ACTUAL
    print("--- MODO CLIENTE ---")
    C_USUARIO = input("Usuario: ")
    C_CLAVE = input("Clave: ")

    threading.Thread(target=c_hilo_polling, daemon=True).start()

    os.system("cls" if os.name == "nt" else "clear")
    print("Hola " + str(C_USUARIO) + ". Usa @Nombre para empezar.")

    while C_RUNNING:
        txt = input()
        if txt:
            if begins(txt, "@salir"):
                C_RUNNING = False
            elif begins(txt, "@lista"):
                print("\nChats:")
                local_mutex.acquire()
                try:
                    try:
                        all_files = os.listdir()
                    except Exception:
                        all_files = []
                    prefix = "LOG_" + str(C_USUARIO) + "_"
                    i = 0
                    while i < len(all_files):
                        name = all_files[i]
                        ok_txt = name[-4:] == ".txt"
                        if begins(name, prefix) and ("_tmp" not in name) and ok_txt:
                            contacto = name.replace(prefix, "").replace(".txt", "")
                            print("- @" + contacto)
                        i += 1
                finally:
                    local_mutex.release()
            elif begins(txt, "@"):
                parts = txt.split(":")
                dest = parts[0].replace("@", "")
                C_CHAT_ACTUAL = dest
                c_mostrar_chat(dest)
                if len(parts) > 1:
                    c_enviar(dest, ":".join(parts[1:]))
            else:
                if C_CHAT_ACTUAL:
                    c_enviar(C_CHAT_ACTUAL, txt)
                else:
                    print("Selecciona chat con @Nombre")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print("=== WHATSAPP CONSOLA ===")
    print("1. Iniciar SERVIDOR")
    print("2. Iniciar CLIENTE")
    op = input("Opción: ")
    if op == "1":
        main_servidor()
    elif op == "2":
        main_cliente()
