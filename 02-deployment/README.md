# 🚀 Deploying the Web App to Azure Container Apps via Azure Container Registry

This guide walks you through deploying your Dockerized web app to **Azure Container Apps** using **Azure Container Registry (ACR)**.

---

## 🛠️ Prerequisites

Ensure you have the following before getting started:

- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) installed and configured.
- Docker installed on your local machine.
- An Azure account with an active subscription.
- Logged into Azure via CLI:  
  [Authenticate with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli-interactively)

---

## 📦 Step 1: Create Azure Container Registry (ACR)

### 1. Open the Azure Portal

![Azure Portal](images/image.png)

### 2. Create a Container Registry

- Click **"Create a resource"**
- Search for **"Container Registry"**

![Search Container Registry](images/image-1.png)

### 3. Click **Create**

### 4. Fill in the registry details:

- **Subscription**: Select your subscription
- **Resource group**: Create or select an existing one
- **Registry name**: Unique name for your ACR
- **Location**: South India
- **SKU**: Basic

![Registry Form](images/image-2.png)

### 5. Click **Review + create**

![Review and create](images/image-3.png)

### 6. Click **Create**

![Create Registry](images/image-4.png)

### 7. Go to the Container Registry

Once deployment is complete:

![Go to resource](images/image-5.png)

### 8. Access Keys

In the registry, navigate to **"Access keys"** in the left-hand menu:

![Access keys](images/image-6.png)

### 9. Note the following:
- **Registry name**
- **Login server**

---

## 🐳 Step 2: Build and Push Docker Image to ACR

### 10. Login to Azure Container Registry

```bash
az acr login --name <your-registry-name>
```

### 11. Build the Docker Image

- Navigate to your project directory where the Dockerfile is located

```bash
cd 01-docker/web-app
```

- Build the Docker image using the following command:

```bash
docker build -t <your-registry-name>.azurecr.io/<your-images/image-name>:<tag> . --platform linux/amd64
```

- Replace `<your-registry-name>`, `<your-images/image-name>`, and `<tag>` accordingly  
  (e.g., `myregistry.azurecr.io/streamlit-app:latest`)

![Build image](images/image-7.png)

### 12. Push the Image to ACR

```bash
docker push <your-registry-name>.azurecr.io/<your-images/image-name>:<tag>
```

![Push image](images/image-8.png)

### 13. Verify the Image in ACR

- In the Azure portal, go to your Container Registry
- Navigate to **Repositories**
- You should see your image listed there

![Repositories](images/image-9.png)

---

## 📲 Step 3: Create a Container App in Azure

### 14. Create a Container App

- Click **"Create a resource"**
- Search for **"Container Apps"**

![Search Container Apps](images/image-11.png)

### 15. Click **Create**

### 16. Fill in the app details:

- **Subscription**: Select your subscription
- **Resource group**: Create or choose one
- **App name**: Unique name for your app
- **Region**: South India
- **Environment**: Create or select existing

![App config](images/image-10.png)

### 17. Configure Container Settings

- Click **Next: Container**
- Choose the image you pushed to ACR

![Container settings](images/image-12.png)

### 18. Configure Ingress

- Click **Next: Ingress**
- Enable ingress
- Set **target port to 8501** (used by Streamlit)

![Ingress settings](images/image-13.png)

### 19. Review and Create

- Click **Next: Review + create**

### 20. Deploy and Access App

- Once deployed, click **Go to resource**  
  *(deployment may take a few minutes)*

![Deployment complete](images/image-14.png)

### 21. Go to Resource

![Go to container app](images/image-15.png)

### 22. Find the App URL

- In the left menu, click **Overview**
- Copy the **URL** of your deployed app

![App URL](images/image-16.png)

### 23. Open Your Streamlit App

- Open the URL in a new browser tab

![Streamlit app](images/image-17.png)

---

## ✅ You're Live!

Your Streamlit app is now successfully deployed using Azure Container Apps via Azure Container Registry 🎉
