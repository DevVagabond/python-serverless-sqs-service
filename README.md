# python-serverless-sqs-service

## Overview

`python-serverless-sqs-service` is a Python-based serverless project designed for creating and managing SQS (Simple Queue Service) producer and consumer services. This project leverages the power of AWS Lambda and AWS SQS to provide a scalable, event-driven architecture without the need for managing servers.

## Features

- **Serverless Architecture**: Built using AWS Lambda, ensuring a cost-effective and auto-scaling solution.
- **SQS Integration**: Seamless integration with AWS SQS for message queuing.
- **Producer and Consumer Services**: Includes both producer and consumer functionalities for SQS messages.
- **Scalable and Reliable**: Designed to handle varying loads efficiently with high reliability.

## Getting Started

### Prerequisites

- AWS Account
- AWS CLI configured with appropriate permissions
- Node.js and NPM
- Serverless Framework
- Python 3.8 or later

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/python-serverless-sqs-service.git
   cd python-serverless-sqs-service

2. **Install dependencies**:
    ```bash
    npm install -g serverless
    pip install -r requirements.txt

### Deployment

```bash
sls deploy
```