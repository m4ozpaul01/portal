#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════
#  KEEP-ALIVE SETUP — run this once with sudo to harden the system
# ═══════════════════════════════════════════════════════════════════════

echo "🔧 Applying system-level keep-alive settings..."

# ── 1. Logind: ignore lid switch, no idle action ──
mkdir -p /etc/systemd/logind.conf.d
cat > /etc/systemd/logind.conf.d/keep-awake.conf << 'EOF'
[Login]
HandleLidSwitch=ignore
HandleLidSwitchExternalPower=ignore
HandleLidSwitchDocked=ignore
IdleAction=ignore
EOF
echo "  ✓ Lid switch disabled (logind)"

# ── 2. Reinforce sleep masking ──
systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target 2>/dev/null
echo "  ✓ Sleep/suspend/hibernate masked"

# ── 3. Disable systemd-oomd (can kill Hermes) ──
systemctl stop systemd-oomd 2>/dev/null
systemctl disable systemd-oomd 2>/dev/null
echo "  ✓ OOM killer disabled"

# ── 4. WiFi power save off via NetworkManager ──
mkdir -p /etc/NetworkManager/conf.d
cat > /etc/NetworkManager/conf.d/wifi-powersave-off.conf << 'EOF'
[connection]
wifi.powersave=2
EOF
echo "  ✓ WiFi power save disabled permanently"

# ── 5. Apply logind settings ──
systemctl restart systemd-logind 2>/dev/null
echo "  ✓ logind restarted"

echo ""
echo "✅ All done! System will stay awake and online."
echo "   Reboot to verify everything sticks."
