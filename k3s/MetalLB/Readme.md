kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.10/config/manifests/metallb-native.yaml
kubectl apply -f values.yaml
kubectl apply -f L2.yaml
