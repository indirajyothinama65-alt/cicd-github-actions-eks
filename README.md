# 🚀 CI/CD Pipeline: GitHub Actions → AWS ECR → AWS EKS

![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)
![AWS](https://img.shields.io/badge/Cloud-AWS-orange)
![Kubernetes](https://img.shields.io/badge/Orchestration-Kubernetes-blue)
![Docker](https://img.shields.io/badge/Container-Docker-blue)
![Python](https://img.shields.io/badge/App-Python%20Flask-green)

## 📌 Project Overview

An end-to-end **production-grade CI/CD pipeline** that automatically builds, 
pushes and deploys a containerized Python Flask application to AWS EKS 
on every git push — with zero manual intervention.

Every code change triggers:
1. GitHub Actions builds Docker image
2. Image tagged with git SHA and pushed to AWS ECR
3. EKS deployment updated with new image
4. Kubernetes rolls out update with zero downtime

---

## 🏗️ Architecture

Developer → Git Push → GitHub Actions
↓
Build Docker Image
↓
Push to AWS ECR
↓
Deploy to AWS EKS
↓
App Live on AWS Load Balancer

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| CI/CD | GitHub Actions |
| Container Registry | AWS ECR |
| Orchestration | AWS EKS (Kubernetes) |
| App | Python Flask + Gunicorn |
| Containerization | Docker |
| Cloud | AWS (ap-south-1) |
| Cluster Setup | eksctl |

---

## 📁 Project Structure
cicd-github-actions-eks/
├── app/
│   ├── app.py              # Flask application
│   └── requirements.txt    # Python dependencies
├── k8s/
│   ├── deployment.yaml     # Kubernetes Deployment
│   └── service.yaml        # Kubernetes LoadBalancer Service
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions Pipeline
├── Dockerfile              # Container definition
└── README.md

---

## ⚙️ Pipeline Stages

### Stage 1 — Build and Push to ECR
```yaml
✅ Checkout source code
✅ Configure AWS credentials
✅ Login to Amazon ECR
✅ Build Docker image (tagged with git SHA)
✅ Push image to ECR
```

### Stage 2 — Deploy to EKS
```yaml
✅ Update kubeconfig for EKS
✅ Replace image placeholder with ECR image URI
✅ Apply Kubernetes manifests
✅ Wait for rollout to complete
✅ Verify pods and service are running
```

---

## 🐳 Dockerfile Highlights
```dockerfile
FROM python:3.11-slim          # Lightweight base image
WORKDIR /app
COPY app/requirements.txt .
RUN pip install -r requirements.txt
COPY app/ .
RUN useradd -m appuser          # Non-root user for security
USER appuser
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

**Security best practices applied:**
- Non-root user
- Minimal base image (slim)
- Layer caching optimization
- Resource limits in Kubernetes

---

## ☸️ Kubernetes Configuration

**Deployment features:**
- Rolling update strategy (zero downtime)
- Liveness probe on `/health` endpoint
- Readiness probe on `/health` endpoint
- CPU and Memory resource limits
- Multiple replicas for high availability

**Service:**
- Type: LoadBalancer (AWS ALB)
- Port 80 → Container port 5000

---

## 🚀 How to Run This Project

### Prerequisites
```bash
# Required tools
aws --version        # AWS CLI
kubectl version      # kubectl
eksctl version       # eksctl
docker --version     # Docker
```

### Step 1 — Configure AWS
```bash
aws configure
# Enter your Access Key, Secret Key, Region: ap-south-1
```

### Step 2 — Create EKS Cluster
```bash
eksctl create cluster \
  --name my-eks-cluster \
  --region ap-south-1 \
  --nodegroup-name general \
  --node-type t3.small \
  --nodes 1 --nodes-min 1 --nodes-max 2 \
  --managed
```

### Step 3 — Create ECR Repository
```bash
aws ecr create-repository \
  --repository-name cicd-demo \
  --region ap-south-1
```

### Step 4 — Add GitHub Secrets
AWS_ACCESS_KEY_ID      → Your IAM Access Key
AWS_SECRET_ACCESS_KEY  → Your IAM Secret Key
AWS_ACCOUNT_ID         → Your AWS Account ID

### Step 5 — Push Code
```bash
git push origin main
# Pipeline triggers automatically! ⚡
```

---

## 📸 Screenshots

### ✅ GitHub Actions — Pipeline Success
![GitHub Ations Pipeline](https://github.com/user-attachments/assets/c69c2f7a-284e-4e59-a6c4-1d1abbaa492d)

### ✅ AWS ECR — Docker Image Pushed
![ECR Image](https://github.com/user-attachments/assets/c4891667-3dea-4f4b-bc76-1168cbe34a47)

### ✅ Kubernetes Pods Running
![kubectl get pods](https://github.com/user-attachments/assets/4b83636b-0395-446b-904f-9f29df3fdfad)

### ✅ LoadBalancer Service
![kubectl get svc](https://github.com/user-attachments/assets/a2c05bfa-9730-43e6-bf52-13020baa6df4)

### ✅ App Live on AWS
![App Live](https://github.com/user-attachments/assets/c667f4b4-f5f6-4e2e-9042-f675e92f3146)

### ✅ EKS Cluster Overview
![EKS Console]()
⚠**Note:** The EKS Cluster was successfully deployed and tested.
            It has been deleted after validation to avoid unnecessary AWS costs.
            Application was verified using kubectl commands.
Key actions performed:
- Cluster creation
- Node group setup
- Application deployment
- verification via kubectl

---

## 🔑 Key Learnings

- Implemented **GitOps principles** — git push triggers full deployment
- Used **git SHA as image tag** for full traceability and rollback capability
- Applied **Kubernetes health probes** for zero-downtime deployments
- Configured **AWS IAM least privilege** for secure pipeline execution
- Built **multi-stage pipeline** with dependency between jobs

---

## 💰 Cost Optimization

- Used `t3.small` instances for cost efficiency
- Single NAT Gateway to reduce data transfer costs
- Cluster deleted after demo to avoid ongoing charges
- ECR lifecycle policies to clean old images

---

## 🧹 Cleanup
```bash
# Delete EKS cluster (stops billing)
eksctl delete cluster \
  --name my-eks-cluster \
  --region ap-south-1

# Delete ECR repository
aws ecr delete-repository \
  --repository-name cicd-demo \
  --region ap-south-1 \
  --force
```

---

## 👩‍💻 Author

**Indira Jyothi Nama**
DevOps Engineer | AWS | Kubernetes | Terraform | CI/CD

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/indira-jyothi-nama)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/indirajyothinama65-alt)
