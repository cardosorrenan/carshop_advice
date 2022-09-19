# Carshop Advice API

### Description

Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It’s a small town, so the mayor had a bright idea to limit the number of cars a person may possess.
- One person may have up to 3 vehicles. 
- The vehicle, registered to a person, may have one color, ‘yellow’, ‘blue’ or ‘gray’. And one of three models, ‘hatch’, ‘sedan’ or ‘convertible’.
- Carford car shop want a system where they can add car owners and cars.
- Car owners may not have cars yet, they need to be marked as a sale opportunity. 
- Cars cannot exist in the system without owners.

---

### Setup
```
git clone https://github.com/cardosorrenan/carshop_advice.git

cd /carshop_advice

docker-compose up --build
```

### Docs
```
http://localhost:5000/apidocs/#/
```

### How docs
```
1. Open swagger http://localhost:5000/apidocs/#/
2. Register a user
3. Login user and copy the access key
4. Paste in the Authorization header field in every request you are going to use
5. Example: Authorization: Bearer {access key}
6. Try it out
```

### Run Tests
```
docker exec -it api bash

pytest
```