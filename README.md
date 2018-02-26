# My-Gallery

This appp enables you to view images from different categories and location.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Activate virtual __source virtual/bin/activate__
* Download Django 1.11 __pip install django==1.11__
* Download Pillow __pip install pillow__
* Download Bootsrap __pip install bootstrap__


### Installing

* Running The server

__python3 manage.py runserver__


## Running the tests

* Method for testing Instance
* Method for saving Image 

### Break down into end to end tests

def test_save_method(self):
            self.mygallery.save_images()
            gallery = Gallery.objects.all()
            self.assertTrue(len(gallery) > 0)

this method allows you to save an image


## Deployment

Add additional notes about how to deploy this on a live system

## Versioning

I used [Python 3.6.3](https://www.python.org/doc/) for versioning. 

## Authors

* **Pascal Oseko** - (https://github.com/pascaloseko)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* To all my classmates Joshua,Victoria,Karush,Patrick,Seth,Sam
