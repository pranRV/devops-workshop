
# Setting CI/CD with GitHub Actions

1. In Azure Portal, navigate to your Container App.
2. Click on **"Deployment"** in the left menu.
![alt text](image.png)
3. Sign in with GitHub.
4. Authorize Azure to access your GitHub account.
5. Select the repository and branch you want to deploy from.
6. In Registry Settings, select your Azure Container Registry.
7. In Image and Tag, select the image you want to deploy.
8. Update the Dockerfile location to the following: `01-docker/web-app/Dockerfile`
![alt text](image-2.png)
9. Click **"Start Continuous Deployment"**.
10. In the github repository, navigate to the **Actions** tab. 