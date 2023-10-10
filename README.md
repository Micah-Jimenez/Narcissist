# Narcissist
    #### Video Demo:  <https://youtu.be/xYOiOSf8RXo>
    #### User Description:

        This project was my solution to a very niche problem. Imagine that you and some friends 
    were out having fun and taking some pictures along the way. At the end of the night one of your friends
    sends all the pictures taken that day to everyone. You love having all the pictures of your friends but a
    decent amount of the photos taken don't have you in them. So, rather narcissistically you want to save 
    in a separate folder only the pictures with you in them. "Narcissist" is the solution to that problem.

        The way the program works is that you input as a command-line-argument the path of a reference
    picture of yourself and the path of the folder of images that you would like Narcissist to sift
    through. If the command-line-arguments you provided are valid then Narcissist will create a new folder 
    named "Narcissist". Then it will go through every picture in the images folder that you provided and 
    save every picture ,that you make an appearance in, to the new folder. If no matches are found Narcissist 
    will print  "No matches found" and delete the new "Narcissist" file that was created.


    #### Technical Description:

        Narcissist utilizes the face_recognition, os, sys, and PIL Python libraries.
    The star of the show is really the face_recognition library. I knew I wanted to utilize it before
    I even had an idea of what my final project would be. I made use of the face_encodings and compare_faces
    functions to have the program look at a picture, make note of all the faces, and finally compare all of
    them to the reference picture. If one of the faces was a match we would then save that picture to the new
    folder using the os and PIL libraries.

        The part of this project that was the most difficult and time consuming was making sure that the user's
    input was valid. For example [What if the user swapped the reference and the image folder in the command line?
    What if the user inputs too many or too few command-line-arguments? What if the user's reference picture isn't a
    image file? what if a file in the user's images folder is not an image?] And even after we get a valid input,
    What is to happen in the case that there are no matches found? All of these questions I had to create solutions
    for and then test that they behaved properly with the use of unit-testing my functions with pytest.

        All and all, this project was a lot of fun. It's really cool to create a solution to a real-life problem.
    Along the way I learned a lot about file I/O and reading documentation. It was a great learning experience,
    and I'm very proud of the final product.