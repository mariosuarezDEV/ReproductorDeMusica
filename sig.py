import signal

# Estado del reproductor
player_state = {
    'playing': False,
    'paused': False,
    'double_speed': False
}

def ctrl_c_handler(signum, frame):
    if player_state['double_speed']:
        print("Reproducción normal")
        player_state['double_speed'] = False
    elif not player_state['playing']:
        print("Reproduciendo música")
        player_state['playing'] = True
    elif player_state['paused']:
        print("Reanudando música")
        player_state['paused'] = False
    else:
        print("Pausa en la música")
        player_state['paused'] = True

def ctrl_z_handler(signum, frame):
    if player_state['playing']:
        print("Música detenida")
        player_state['playing'] = False

def ctrl_x_handler(signum, frame):
    if not player_state['double_speed']:
        print("Reproducción al x2")
        player_state['double_speed'] = True

# Asociar señales a los manejadores
signal.signal(signal.SIGINT, ctrl_c_handler)  # Ctrl+C
signal.signal(signal.SIGTSTP, ctrl_z_handler)  # Ctrl+Z
signal.signal(signal.SIGQUIT, ctrl_x_handler)  # Ctrl+X

print("Reproductor de música simulado. Usa las señales para controlar la reproducción.")

# Mantener el programa ejecutándose hasta recibir una señal diferente a las manejadas
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nPrograma cerrado manualmente.")
