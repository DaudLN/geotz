# Django API Project

This is a Django project that provides an API for managing regions, districts, and wards.

## Project Structure

The project follows a standard Django project structure with the following main components:

- `api/`: Django app for the API implementation.
- `api/models.py`: Contains the model definitions for Region, District, and Ward.
- `api/serializers.py`: Serializers for converting model instances to JSON representations.
- `api/views.py`: Viewsets for handling API requests and responses.
- `api/urls.py`: URL configuration for the API endpoints.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/your-repository.git
   ```

2. Navigate to the project directory:

   ```shell
   cd your-repository
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python3 -m venv env
   source env/bin/activate
   ```

4. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

5. Apply the database migrations:

   ```shell
   python manage.py migrate
   ```

6. Start the development server:

   ```shell
   python manage.py runserver
   ```

7. Access the API endpoints in your browser or using an API client like cURL or Postman.

## API Endpoints

The following API endpoints are available:

- `GET /regions/`: Get a list of all regions.
- `POST /regions/`: Create a new region.
- `GET /regions/{slug}/`: Get details of a specific region.
- `PUT /regions/{slug}/`: Update a specific region.
- `DELETE /regions/{slug}/`: Delete a specific region.

- `GET /regions/{region_slug}/districts/`: Get a list of all districts in a region.
- `POST /regions/{region_slug}/districts/`: Create a new district in a region.
- `GET /regions/{region_slug}/districts/{slug}/`: Get details of a specific district in a region.
- `PUT /regions/{region_slug}/districts/{slug}/`: Update a specific district in a region.
- `DELETE /regions/{region_slug}/districts/{slug}/`: Delete a specific district in a region.

- `GET /regions/{region_slug}/districts/{district_slug}/wards/`: Get a list of all wards in a district.
- `POST /regions/{region_slug}/districts/{district_slug}/wards/`: Create a new ward in a district.
- `GET /regions/{region_slug}/districts/{district_slug}/wards/{slug}/`: Get details of a specific ward in a district.
- `PUT /regions/{region_slug}/districts/{district_slug}/wards/{slug}/`: Update a specific ward in a district.
- `DELETE /regions/{region_slug}/districts/{district_slug}/wards/{slug}/`: Delete a specific ward in a district.

## Permissions

The API endpoints are protected by permissions. By default:

- Anonymous users can view the regions, districts, and wards.
- Only authenticated admin users can create, update, and delete regions, districts, and wards.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to customize the README.md file further based on the specific details and requirements of your project.
