

# Create venv
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Install main packages 
pip install fastapi uvicorn starlette pydantic pandas

# Freeze libraries
pip freeze > requirements.txt

# Command to start the fastapi
uvicorn main:app --reload

# Check whether it's working
curl localhost:8000

# Builf ci-api image
docker build -t ci-api-img .

docker run --name ci-api-ctn -p 80:80 ci-api-img

NM_IMAGE="ci-api-img"
NM_DOCKER_USER="guigo13"

docker tag ci-api-img guigo13/ci-api-img

docker push guigo13/ci-api-img

docker tag guigo13/ci-api-img gcr.io/ci-gcp-proj/ci-api-img

docker push gcr.io/ci-gcp-proj/ci-api-img



