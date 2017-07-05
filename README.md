# MSC website on GITHUB
A template for the website is here: [aliwang2001.github.io](https://aliwang2001.github.io)
(note: to make it as real as possible, I just added random blurbs of text and some nice pictures of caltech lol)
The MSC website will now be hosted on GitHub. This will allow everyone to be able to collaborate and help make the website amazing for the public. A copy of all website files will be on a folder in the server, and someone familiar with GitHub will update the website every week or so.

## Things you can do
* Add your contact card to the group page, optional info to display is picture, email, cell, or personal page (Scroll down)
* Add your own, personal page, with functions such as displaying a bio, a calendar with your schedule, anything. 
* Add a cool research article you found interesting on the home page and in the research archive.
* Add your own exciting research and present it through a slideshow.

No HTML/CSS experience necessary, all you have to do is follow the HTML template and copy/paste in the right location ^^

## Creating your own contact card

OPTIONAL: copy and paste "python /ul/aliwang/website/contactcard.py" into the wag server, and follow directions as shown. You don't need to read the rest of this boring guide to create your contact card.



Please put your desired image in the /images/profilepics folder. If not, you can also provide the URL of your image. If you do not wish to put a picture, just use the path "images/profilepics/nopic.png" which will display the default profile picture.

Tips: everything in HTML has a start tag and end tag, which has a slash

I will be walking you through all the parts, so please have a text editor open with the following template copied and pasted.

```html
                              <!-- TEMPLATE START -->
                              
                              <!-- add your category -->
                              <div class="iso-box director col-md-3 col-sm-6">
                                 <div class="portfolio-thumb">
                                    <!-- image link -->
                                    <img src="images/profilepics/nopic.png" class="img-responsive" alt="Portfolio">

                                       <div class="portfolio-overlay">
                                            <div class="portfolio-item">
                                                  <!-- Items here will be displayed by hovering over image -->
                                                  <h2>(000)000-0000</h2>
                                                  <h2><a href="mailto:aliwang2001@gmail.com">email</a></h2>
                                                  <h2><a href="personalpages/persona.html">Personal Page</a></h2>
                                            </div>
                                       </div>
                                 </div>
                                 <!-- Items here will be displayed under picture -->
                                 <h6>Person A</h6>
                                 <h5>Director of Chemistry</h5>
                                 <h5><a href="mailto:myemail@gmail.com">myemail@gmail.com</a></h5>
                              </div>
                              <!-- TEMPLATE END -->
```

### Category

Find this line. In the quotation marks, after "iso-box" and before "col-md-3", please add what category you belong in.
For example, the following is for someone who is a director:

```html
 <div class="iso-box director col-md-3 col-sm-6">
```
Graduate:
```html
 <div class="iso-box grad col-md-3 col-sm-6">
```
Undergraduate:
```html
 <div class="iso-box undergrad col-md-3 col-sm-6">
```
Postdoc:
```html
 <div class="iso-box postdoc col-md-3 col-sm-6">
```
Staff:
```html
 <div class="iso-box staff col-md-3 col-sm-6">
```
Please use the exact words in order for the program to run correctly.
Need another category? Please email [aliwang2001@gmail.com](mailto:aliwang2001@gmail.com)

### Information displayed under the picture

**Name** is added under the comment "Items here will be displayed under picture".
Please write your name in between the <h6> and </h6> tags.

**Additional information(such as a major)** is added between the <h5> and </h5> tags.


For example:
```html
            <!-- Items here will be displayed under picture -->
            <h6>Person A</h6>
            <h5>Director of Chemistry</h5>
            <h5><a href="mailto:myemail@gmail.com">myemail@gmail.com</a></h5>
```
To display the **email** under the picture box, please replace your email with "myemail@gmail.com".
If you do not want to display your email under the box, delete the whole line.

For anything you do not want to display, just delete the whole line.

### Information displayed by hovering over the picture

```html
             <!-- Items here will be displayed by hovering over image -->
             <h2>(000)000-0000</h2>
             <h2><a href="mailto:aliwang2001@gmail.com">email</a></h2>
             <h2><a href="personalpages/persona.html">Personal Page</a></h2>

```
For **email and cell phone**, please replace the information in the example with your personal information.
For anything you do not wish to display, please delete the line.

To provide a **link to your personal page**, please change the pathname to the path of your .html file of your personal page. For example, a path would be "personalpages/aliwang.html". See the next section on creating your own page.


## Adding article to home page

OPTIONAL: Copy and paste "python /ul/aliwang/website/homearticle.py" into WAG server. You may skip the instructions below.


Copy and paste the section below. Comments are in the code and will act as a guide.


```html
<!-- TEMPLATE START
          ================================================== -->

          <div class="row">
          <div class="wow fadeInUp col-md-6 col-sm-6" data-wow-delay="1s">
              <div class="blog-thumb">
                    <!-- You can link your post to a separate article. If you don't want to, replace the link section with a hastag (#) -->
                    <a href="COPY AND PASTE LINK HERE"><h1>This is the title of your article.</h1></a>
                     <div class="post-format">
                     <!-- you can link the Author name to your personal page. If not, leave the hastag. -->
                        <span>By <a href="#">YOUR NAME HERE</a></span>
                     <!-- replace the date here -->
                        <span><i class="fa fa-date"></i>5 June 2016, Sunday</span>
                     </div>
                     <!-- write a paragraph about your post here.-->
                     <p>This is a paragraph. Write whatever you want in here.</p>
                    <!-- this is a button. Put the link to your post (the one you used earlier) here. If not, delete the next line. -->
                    <a href="COPY AND PASTE LINK HERE" class="btn btn-default">Read More</a>
              </div>
          </div>

          <!-- SLIDESHOW START
          ================================================== -->
          <div class="wow fadeInUp col-md-6 col-sm-6" data-wow-delay="0.5s">
                   <div class="slideshow-container">
                   
                   <!-- These little chunks are a "slide". You can have as many as you want, just keep copying and pasting. Each features a picture link. Either place your image in the images/articlepics/ folder and type its path or copy/paste its URL. --> 
                   <!--Slide Template start-->
                            <div class="mySlides fade">
                            <!-- make sure to have the numbers change for what number the slide is/ how many slides in total -->
                              <div class="numbertext">1 / 4</div>
                              <!-- link your picture -->
                              <img src="images/articlepics/YOURPICTURENAME.jpg" style="width:100%">
                              <!-- You can include a caption if you prefer, if not, delete the line. -->
                              <div class="text">Caption Text</div>
                            </div>
                    <!-- Slide Template end -->
                    
                            <div class="mySlides fade">
                              <div class="numbertext">2 / 4</div>
                              <img src="images/articlepics/YOURPICTURENAME.jpg" style="width:100%">
                              <div class="text">Caption Two</div>
                            </div>

                            <div class="mySlides fade">
                              <div class="numbertext">3 / 4</div>
                              <img src="images/articlepics/YOURPICTURENAME.jpg" style="width:100%">
                              <div class="text">Caption Three</div>
                            </div>
                            
                              <div class="mySlides fade">
                              <div class="numbertext">4 / 4</div>
                              <img src="images/articlepics/YOURPICTURENAME.jpg" style="width:100%">
                              <div class="text">Caption Four</div>
                            </div>

                        <a class="prev">&#10094;</a>
                        <a class="next">&#10095;</a>

                          <!-- Count how many slides you have in total. Copy and paste the dots to have the same number. For example, the following is for 4 slides. -->
                            <div style="text-align:center">
                              <span class="dot"></span>
                              <span class="dot"></span>
                              <span class="dot"></span>
                              <span class="dot"></span>
                            </div>
                  </div>
          </div>
          <!-- SLIDESHOW END
          ================================================== -->
         </div>

<!-- Template END
================================================== -->
```
Don't want a slideshow? Replace the slideshow template (from start to end) with:

```html
<div class="wow fadeInUp col-md-6 col-sm-6" data-wow-delay="0.5s">
<!--Put picture path below, or replace with URL -->
<img src="images/articlepics/YOURPICTURENAME.jpg" style="width:100%">
</div>

```

## Creating your own personal page

This section will be updated soon.

```
HTML Template will appear here...
```


## Questions? Concerns? Comments? Tips/advice?

Please feel free to email [aliwang2001@gmail.com](mailto:aliwang2001@gmail.com) if you need any help setting anything up.
Tips and advice on how to make the website look even better is greatly appreciated!
If you encounter anything weird in the formatting, please email. Thank you for the help!

## Happy 4th of July!!
**Alicia Wang**
  
