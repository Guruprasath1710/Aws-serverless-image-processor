# AWS Serverless Image Processor

A Python-based image processing application designed with a serverless architecture in mind. The project demonstrates image manipulation, validation, logging, automated testing, and a clean project structure suitable for AWS Lambda deployment.

## Features

- Resize images
- Convert images to grayscale
- Rotate images
- Compress images
- Image validation
- Logging support
- Automated unit testing with Pytest
- Modular project architecture

## Project Structure

```
aws-serverless-image-processor/
│
├── app/
│   ├── processor.py
│   ├── validator.py
│   ├── logger.py
│   ├── config.py
│   └── __init__.py
│
├── image/
│   └── sample.jpg
│
├── output/
│
├── lambda/
│   └── lambda_function.py
│
├── tests/
│   ├── test_processor.py
│   ├── test_negative.py
│   └── test_invalid_parameters.py
│
├── requirements.txt
└── README.md
```

## Technologies Used

- Python 3
- Pillow
- Pytest
- Git
- GitHub

## Installation

Clone the repository

```bash
git clone https://github.com/Guruprasath1710/Aws-serverless-image-processor.git
```

Navigate to the project

```bash
cd Aws-serverless-image-processor
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

```bash
py -m lambda.lambda_function
```

## Running Tests

```bash
py -m pytest
```

## Test Coverage

The project includes:

- Functional Tests
- Negative Tests
- Invalid Parameter Tests

**Total Tests:** 15

**Status:** All tests passing

## Future Improvements

- AWS Lambda deployment
- Amazon S3 integration
- REST API with API Gateway
- Docker support
- CI/CD using GitHub Actions

## Author

**Guruprasath**

GitHub:
https://github.com/Guruprasath1710