# Book Recommender Backend
Central hub for a community-driven platform focused on sharing and exploring book recommendations.

## Overview
- [Setup Instructions](#setup-instructions)
- [Project Extension Developer Guide (Custom API)](#project-extension-developer-guide-custom-api)

## Setup Instructions

### Prerequisites
- Docker

### Installation

1. **Clone the repository:**
```bash
   git clone https://github.com/Abhishek-jha-96/book-recommender-backend.git
   cd book-recommender-backend
```
2. Update the .env file according to your use

3. Run the application in the Docker Container:

```bash
docker compose up --build -d
```
4. Apply migrations:

In the running container:

```bash
docker-compose exec <container> python manage.py migrate
```
## Project Extension Developer Guide (Custom API)
### this guide covers:
- Setting up Django: Installation and project creation.
- Defining Models: How to create and manage models.
- Serializers: How to use serializers for data validation and transformation.
- Views and ViewSets: Implementing different types of views.
- URL Routing: Mapping views to URLs.
- Authentication: Protecting API endpoints.
- Documentation: Using tools like Swagger for API documentation.

### Setting Up the Environment
**Installation instructions are provided above.**

1. **Create a New App**
```bash
Copy code
django-admin startapp books
```
2. Defining Models
    Example Model: Personalized Reading List
```python
from django.db import models
from django.contrib.auth.models import User

class PersonalizedReadingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_lists')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```
3. **Creating Serializers**
```python
from rest_framework import serializers
from .models import PersonalizedReadingList

class PersonalizedReadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalizedReadingList
        fields = ['id', 'user', 'title', 'description', 'created_at', 'updated_at']
```
4. **Defining Views**
```python
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PersonalizedReadingList
from .serializers import PersonalizedReadingListSerializer

class PersonalizedReadingListViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalizedReadingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PersonalizedReadingList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```
5. **URL Routing**
``` python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonalizedReadingListViewSet

router = DefaultRouter()
router.register(r'reading-lists', PersonalizedReadingListViewSet, basename='readinglist')

urlpatterns = [
    path('', include(router.urls)),
]
```

6. **Updating settings.py**
Don't forget to update settings.py according to your changes, including adding the new app and any required configurations.


## Best Practices
- CRUD Operations: Ensure all CRUD operations (Create, Read, Update, Delete) are implemented where necessary.
- Authentication: Use Django Rest Framework's authentication classes to protect endpoints.
- Data Validation: Utilize serializers for data validation.
- Pagination: Implement pagination for endpoints returning large datasets.
- Throttling: Use throttling to prevent abuse of your API.

## Git best Practices
for, functional area and stability-based branching strategy. The general categorisation is as follows -

1. `main` : This branch contains the fully-tested stable code. And this is the one that is generally deployed on production.
2. `develop` : This branch contains the code that the development team is working on. Essentially not a tested code. Usually, deployed on the an environment that is used by developers for testing.
3. `feature` : These branches are the individual branches that represent a particular feature or fix that a developer is working on and eventually would be merged to the develop branch.
4. `release` : These branches are used to make the config changes right before a release or deployment.

## Contributing

For detailed Git commit styleguide, refer to the guide below:

- [Git Commit Styleguide](https://udacity.github.io/git-styleguide/)
