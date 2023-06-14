from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


def get_proton_vpn_ips():
    response = requests.get("https://api.protonmail.ch/vpn/logicals")
    data = response.json()
    return [
        server["ExitIP"]
        for logical_server in data["LogicalServers"]
        for server in logical_server["Servers"]
    ]


@app.route("/check_ip", methods=["GET"])
def check_ip():
    ip_address = request.args.get("ip")
    proton_vpn_ips = get_proton_vpn_ips()
    return jsonify({"protonvpn": ip_address in proton_vpn_ips})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4242)
