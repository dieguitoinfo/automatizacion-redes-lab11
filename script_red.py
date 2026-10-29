# ===================================================
# SCRIPT DE AUTOMATIZACIÓN DE REDES - MÓDULO DE VLANs
# ===================================================

def aplicar_vlan():
    vlan_id = 100  # Modificado para segmento Administrativo
    nombre_vlan = "VENTAS"
    print(f"[+] Configurando en Switch Core: VLAN {vlan_id} ({nombre_vlan})")

if __name__ == "__main__":
    print("=== INICIANDO DESPLIEGUE EN SW-CORE-01 ===")
    aplicar_vlan()