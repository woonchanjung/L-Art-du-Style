<div align="center">

# L'Art du Style

### Built by: **[Woonchan Jung](https://www.linkedin.com/in/woonchanjung/)**

![](https://i.imgur.com/6tFAwmD.png)

<hr></hr>
  
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
![Maintainer](https://img.shields.io/badge/Maintainer-woonchanjung-blue)
![Ask](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)

![Django](https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![CSS](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)

![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Heroku badge](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

<hr></hr>

## **[CLICK HERE](https://l-art-du-style.herokuapp.com/)**
</div>

## Roadmap
**[TRELLO](https://trello.com/invite/b/YNOmug6P/ATTI4962d7f8e6953edeabe7a6124f49a00b410FB9C7/lart-du-style)**
/
**[Wireframe](https://whimsical.com/wireframe-X1qVJ6RKy1Aw2EboRopKNd)**
/
**[ERD](https://whimsical.com/erd-EAAHEkc3FiN56FSpNYiW5U)**

### Description:

Welcome to L'Art du Style - a Django-based web application that helps users test their fashion sense by allowing them to upload photos of their clothing items and see if they match. L'Art du Style is the ultimate tool for those looking to elevate their fashion game and make sure their outfits always look stylish and put-together.

Features:
- Upload and compare clothing items: Users can upload images of their tops and bottoms, and the application will provide feedback on how well they match.
- View and delete matches: Users can view their previously created matches and delete them if desired.
- Explore match history: The application keeps track of the user's match history, allowing them to revisit and analyze their fashion choices over time.

<hr></hr>

<div align="center">

<h2>Landing Page</h2>

<p align="center">
<img src="https://i.imgur.com/SDCSsL8.png" width=50% height=50% align="center">
</p>
<hr></hr>
 
<h2>SignUp/SignUp Page</h2>

<p align="center">
<img src="https://i.imgur.com/ycPlhzg.png" width=50% height=50% align="center">
<hr></hr>
<img src="https://i.imgur.com/lwGDuZ4.png" width=50% height=50% align="center">
</p>
<hr></hr>
 
<h2>My Closet</h2>

<p align="center">
<img src="https://i.imgur.com/1SMCBkE.png" width=50% height=50% align="center">
</p>
<hr></hr>

<h2>Upload Top/Bottom</h2>

<p align="center">
<img src="https://i.imgur.com/Ndw4osW.png" width=50% height=50% align="center">
</p>
<hr></hr>
<p align="center">
<img src="https://i.imgur.com/mq9E0X7.png" width=50% height=50% align="center">
</p>
<hr></hr>

<h2>Create Match</h2>

<p align="center">
<img src="https://i.imgur.com/Sy0fi7R.png" width=50% height=50% align="center">
</p>
<hr></hr>

<h2>View Matches</h2>

<p align="center">
<img src="https://i.imgur.com/L38FFQU.png" width=50% height=50% align="center">
</p>
<hr></hr>

</div>

<div align="center">

 <h2>The Code Behind The Program</h2>
</div>

```
def create_match(request):
    user_tops = Top.objects.filter(user=request.user)
    user_bottoms = Bottom.objects.filter(user=request.user)

    if user_tops.exists() and user_bottoms.exists():
        if request.method == 'POST':
            top_id = request.POST.get('top')
            bottom_id = request.POST.get('bottom')
            top = get_object_or_404(Top, id=top_id, user=request.user)
            bottom = get_object_or_404(Bottom, id=bottom_id, user=request.user)

            match = Match(user=request.user, top=top, bottom=bottom)
            match.save()

            return redirect('view_matches')
        else:
            tops = Top.objects.filter(user=request.user)
            bottoms = Bottom.objects.filter(user=request.user)
            return render(request, 'clothes/create_match.html', {'tops': tops, 'bottoms': bottoms})
    else:
        message = "Please upload at least one top and one bottom to create a match."
        return render(request, 'clothes/create_match.html', {'message': message})
```

<div align="center">
 <h2> Future IceBox </h2>
</div>

- Add social sharing functionality: Allow users to share their fashion matches on social media platforms to showcase their styling skills.
- User feedback and rating system: Implement a user feedback and rating system where users can provide feedback on the matches and rate the accuracy of the fashion suggestions.
- Advanced matching algorithms: Enhance the matching algorithms to consider additional factors such as color coordination, style compatibility, and seasonal appropriateness.
- Integration with online fashion retailers: Provide links or suggestions to online fashion retailers where users can purchase clothing items similar to their matches.

Acknowledgements: 
- Kenneth C.
- Matthew G. 
- Evan M.
- Payne F.

Written for **General Assembly Software Engineering Immersive Bootcamp**
