https://www.fullstaq.com/knowledge-hub/blogs/setting-up-your-own-k3s-home-cluster

kubectl create namespace traefik

helm install traefik traefik/traefik -n traefik -f values.yaml

kubectl port-forward deploy/traefik 9000 -n traefik

http://localhost:9000/dashboard/#/


helm upgrade -f values.yaml traefik stable/traefik -n traefik
