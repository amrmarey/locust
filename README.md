
# 🌟 Locust Load Testing Project

[![Locust](https://img.shields.io/badge/Locust-Performance%20Testing-green?style=flat&logo=python)](https://docs.locust.io/)  
Effortlessly simulate and measure the performance of your web applications with **Locust**. This project leverages **Docker** to enable scalable and distributed load testing.

---

## 🗂️ Project Structure

```plaintext
.
├── docker-compose.yml   # Docker Compose configuration for Locust master and workers
├── locustfile.py        # Locust test scenarios (tasks) for load testing
└── README.md            # Project documentation
```

---

## 🛠️ Prerequisites

Make sure you have the following installed on your system:

- **[Docker](https://www.docker.com/)**  
- **[Docker Compose](https://docs.docker.com/compose/)**  

---

## 🚀 How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/amrmarey/locust.git
   cd locust
   ```

2. **Start Locust with Docker Compose**:
   Launch Locust master and workers:
   ```bash
   docker-compose up --scale worker=4 
   ```

3. **Access the Locust Web Interface**:
   Open your browser and navigate to:
   ```plaintext
   http://localhost:8089
   ```

4. **Run the Load Test**:
   - Enter the target host (e.g., `http://example.com`).
   - Configure the number of users and spawn rate.
   - Start the test and monitor real-time results.

---

## 📝 Example `locustfile.py`

The `locustfile.py` defines the tasks for load testing. Below is an example included in this project:

```python
from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_home(self):
        self.client.get("/")
```

### What It Does
- Simulates users visiting the `/` endpoint of your target host.

---

## 📈 Scaling Locust Workers

You can easily scale the number of workers to increase the load:

```bash
docker-compose up --scale worker=<number_of_workers>
```

For example, to run 10 workers:
```bash
docker-compose up --scale worker=10
```

---

## 🧹 Cleaning Up

To stop and clean up the containers and associated network:
```bash
docker-compose down -v
```

---

## 🔧 Troubleshooting

- **File Not Found Errors**:
  - Ensure `locustfile.py` exists and is properly mounted in `docker-compose.yml`.

- **Web Interface Not Accessible**:
  - Ensure port `8089` is not blocked or used by another application.

---

## 🌍 Contribute

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature XYZ"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request. 🎉

For questions or suggestions, feel free to contact **Amr Marey** at 📧 [amr.marey@msn.com](mailto:amr.marey@msn.com).

---

## 📚 Additional Resources

- 🌐 [Locust Official Documentation](https://docs.locust.io/)  
- 🐋 [Docker Compose Documentation](https://docs.docker.com/compose/)  

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

- **Amr Marey**  
- ✉️ [amr.marey@msn.com](mailto:amr.marey@msn.com)  
- 🌟 [GitHub Profile](https://github.com/amrmarey)

---

### 🔗 Keywords for SEO
`Locust`, `Load Testing`, `Performance Testing`, `Docker`, `Python`, `Scalable Load Testing`
