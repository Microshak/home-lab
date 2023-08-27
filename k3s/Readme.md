Uninstall

```
/usr/local/bin/k3s-uninstall.sh
```

# Install
without traffic and servicelb
```
curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.24.8+k3s1  INSTALL_K3S_EXEC="server --disable traefik --disable servicelb" sh -
```



# Token (secrete)
```
cat /var/lib/rancher/k3s/server/token
```

# Config
```
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/k3s.yaml
```
copy to ~/.bashrc

```
export KUBECONFIG=~/.kube/k3s.yaml
```