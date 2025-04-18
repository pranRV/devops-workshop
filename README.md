# DevOps Workshop — **From Code to Cloud**
_Facilitated by: Rithin Chalumuri_

---

## 🧑‍💼 About Me

Hi! I’m **Rithin Chalumuri**.

I enjoy building products from 0 to 1, and helping others do the same. 

I've worked across startups and tech projects where I’ve experienced systems growing from a single machine to distributed cloud-scale architectures.

GitHub: [github.com/rithinch](https://github.com/rithinch)

---

## 🕒 Agenda

| Time            | Topic                                      |
|-----------------|--------------------------------------------|
| 9:30 - 10:00    | Pre-requisites & Dev Environment Setup     |
| 10:00 - 10:30   | Introduction to DevOps                     |
| 10:30 - 11:30   | Docker: Containers for Developers          |
| 11:30 - 12:30   | Cloud Deployment & Hosting                 |
| 12:30 - 1:30    | Lunch 🍽️                                   |
| 1:30 - 3:00     | Distributed Systems & Scaling Challenges   |
| 3:00 - 4:00     | Infrastructure as Code                     |
| 4:00 - 4:45     | CI/CD with GitHub Actions                  |
| 4:45 - 5:30     | Observability & Monitoring Fundamentals    |
| 5:30 - 6:00     | Real-world Q&A, Wrap-up                    |

---

## 💡 Session: Introduction to DevOps (10:00 - 10:30)

- DevOps = Developers + Operations
- Not a tool, not a job title, a **culture**
- Goal: Shorten time from "code complete" to "customer using it"
- Developers are increasingly responsible for “You build it, you run it” systems
- Key focus: Collaboration, automation, reliability

---

## 🐫 Session: Docker & Containers (10:30 - 11:30)

### Why Containers?

- "It works on my laptop" ✖️
- Portable, consistent environments
- Simplifies deployment across platforms

---

### Dockerfile Breakdown

```Dockerfile
FROM python:3.11-slim      # Base image
WORKDIR /app               # Working directory
COPY . .                   # Copy code into container
RUN pip install -r requirements.txt  # Install dependencies
EXPOSE 8501                # Application port
CMD ["streamlit", "run", "app.py"]   # Start command
```

### Analogy:
- Containers are like standardized shipping containers.
- Server doesn’t care what’s inside; uniform handling.
- Portable between environments without repackaging.

---

## ☁️ Session: Cloud Deployment & Hosting (11:30 - 12:30)

- Cloud = Renting servers on demand
- Popular providers: Azure, AWS, GCP
- Concepts:
   - **Scaling**
   - **Redundancy**
   - **Pay-as-you-go**

| Host Type          | Use Case                 |
|---------------------|--------------------------|
| Virtual Machines    | Manual setup            |
| Containers          | Lightweight deployment  |
| Kubernetes          | Orchestration at scale  |

---

## 🧠 Session: Distributed Systems & Scaling Challenges (1:30 - 3:00)

### What is a Distributed System?

- Components spread over machines, regions, or services
- Connected via network

---

### Why Break Down Systems?

- Scale bottlenecks
- Maintenance headaches
- Risk mitigation (single point of failure)
- Independent deployments and updates

---

### Communication Patterns

| Pattern            | Example        | Pros              | Cons                   |
|---------------------|----------------|--------------------|-------------------------|
| Synchronous         | API Call       | Simple             | Tight coupling, latency|
| Asynchronous        | Message Queue  | Decoupled, resilient| More complexity        |

---

### Real-World Example: UPI System

- Distributed participants: You, Bank, UPI switch, Receiver
- Networked handshakes with retry, consistency, and timeouts
- Eventual consistency

---

### Real-World Example: Swiggy Order Flow

- Customer ➔ Order Service ➔ Restaurant ➔ Delivery Partner ➔ Payment
- Distributed services for reliability and scalability
- Uses both sync (order confirmation) and async (status updates)

---

## 🔧 Session: Infrastructure as Code (3:00 - 4:00)

### What is IaC?

- Define infrastructure as versioned code
- Tools: Terraform, Azure Bicep, CloudFormation
- Benefits: Predictability, repeatability, speed

---

### Terraform Example

```hcl
resource "azurerm_container_group" "app" {
  name                = "my-app-container"
  location            = "East US"
  resource_group_name = "devops-workshop"
  os_type             = "Linux"

  container {
    name   = "app"
    image  = "myregistry.azurecr.io/my-app:latest"
    cpu    = "1"
    memory = "1.5"
    ports {
      port     = 8501
      protocol = "TCP"
    }
  }
}
```

---

## 🚀 Session: CI/CD with GitHub Actions (4:00 - 4:45)

### Why CI/CD?

- Continuous Integration: Automatically test new code.
- Continuous Deployment: Automatically release new code.
- Ensures reliable, repeatable, automated software delivery.

---

### GitHub Actions Example

```yaml
name: Deploy App

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v4

    - name: Build Docker Image
      run: docker build -t my-app .

    - name: Push to Registry
      run: docker push myregistry.azurecr.io/my-app:latest
```

---

## 🤔 Session: Observability & Monitoring Fundamentals (4:45 - 5:30)

### 3 Pillars:

- Logs: What happened?
- Metrics: How much?
- Traces: Where and why?

---

### Example: Debugging Production Issues

1. Metrics spike: Errors increase.
2. Traces: Slow downstream service identified.
3. Logs: Connection limit reached.
4. Deploy fix, observe system recovery.

Tools: Jaeger, OpenTelemetry, Azure Monitor.

---

## 🖊️ Final Wrap-up: The DevOps Loop (5:30 - 6:00)

**Code ➔ Build ➔ Test ➔ Deploy ➔ Monitor ➔ Feedback ➔ Repeat**

- Build with iteration in mind
- Expect failure, design for recovery
- Automate everything
- Focus on team collaboration, not just tools

---

## 🎉 Thank You!

This workshop was about:

- Understanding core concepts, not just tech stacks.
- Building mental models for modern distributed systems.
- Becoming production-ready.

**See you on GitHub:** [github.com/rithinch](https://github.com/rithinch)

