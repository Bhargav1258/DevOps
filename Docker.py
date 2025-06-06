#Docker:
#-------------
'''
Docker is a platform that allows developers to automate the deployment of applications inside lightweight,
portable containers. These containers can run on any system that has Docker installed, making it easier to develop, ship, and run applications consistently across different environments.

is devide into three main parts:

1.Docker : I is a Container Engine that allows you to build, run, and manage containers.
2.Docker Hub : It is a cloud-based registry service where you can store and share Docker images.
                (It is like a container image library)
3.Docker Desktop : It is a GUI application that provides a user-friendly interface 
for managing Docker containers and images on your local machine.

it is used to create, deploy, and run applications by using containers. with collaberation of multiple 
people, it is easy to share and manage applications in a consistent environment.


Applications of Docker:
-----------------------
3 types of applications that can be built using Docker include:
---------------------------------------------------------------
1.Java Applications:(Spring Boot, Java EE Restful APIs)
2.Python Applications:(Flask, Django, FastAPI)
3.Node.js Applications:(react, express.js, Next.js)

              The working Process of Docker:
              ------------------------------
              1.Containerization: Docker packages applications and their dependencies into containers.
              2.Image Creation: Developers create Docker images that contain the application code, libraries, and runtime.
                3.Container Deployment: Docker runs these images as containers, which are isolated environments.
                4.Run the Application: Containers can be started, stopped, and managed independently.
  1.containerization:
  --------------------
  socurce code, libraries, and runtime are packaged into a single unit called a container.
                        (src+libraries+runtime = container)
    2.image creation:
    -------------------
    Docker images are created from the container, which is a lightweight, standalone, and executable package.
    Images are built using a Dockerfile, which contains instructions on how to create the image.
    
    3.container deployment:
    ----------------------
    Docker runs these images as containers, which are isolated environments 
    that can run on any system with Docker installed.   
    
    4.run the application:
    -------------------
    Containers can be started, stopped, and managed independently, allowing for easy deployment and scaling of applications.
    
    
        ==============> Prerequisites for Docker:
        ------------------------------------------
        1.Install the Docker Desktop application on your machine.
        2.Create a Docker Hub account to store and share your Docker images.
        3.Development tools:
        - For Java: Install JDK and a build tool like Maven or Gradle.
        - For Python: Install Python and a package manager like pip.
        - For Node.js: Install Node.js and npm (Node Package Manager).
        4-Text editor or IDE: Use any code editor or integrated development environment (IDE) to write your application code.
             

'''
#Working Process of Docker For Java Applications:
#------------------------------------------------
'''
==>Prerequisites for Docker:
-----------------------------
1.Docker Desktop.
2.Java Development Kit (JDK).(17 or higher)
3.Maven or Gradle (for building Java applications).
4.Text editor or IDE (like IntelliJ IDEA, Eclipse, or Visual Studio Code).

Note:
------
We must have Docker hub account to push our images to the Docker hub.


'''
'''
#Step-by-Step Process to Create a Dockerized Java Application:
----------------------------------------------------------------
Step 1: Create a Java Application
       
       Project Structure: => spring-boot-rest-api
       
Step 2: Create a Dockerfile

# Create a file named Dockerfile in the root of your project directory.
# Dockerfile  ==> spring-boot-rest-api/Dockerfile

Phase 1: Containerization
--------------------------
#Containerization involves preparing your Spring Boot project for Docker by creating a 
# Dockerfile and a "docker-compose.yml" file to define the application and MySQL services.

Phase 2: Image Creation
------------------------
docker build

docker images

Phase 3 : Container Deployment
-------------------------------
step1 : Start the container  : docker-compose up -d 

Step 2 : verify the running containers :  docker ps

Step 3 : verify the logs of the container : docker-compose logs app


Phase 4: Run the Application
#-------------------------------

# mvn spring-boot:run

# After the container is running, you can access your Spring Boot application at http://localhost:8080.

# To stop the container, use: docker-compose down

# To remove the container and its associated resources, use: docker-compose down --volumes

docker-compose down -v






'''