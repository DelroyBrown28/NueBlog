<div class="container col-md-12 my-5 p-0 feature-container flexed">
    {% for post in posts  %}
    {% if post.large_feature == True %}
    <a href="{{post.get_absolute_url}}" class="main-feature-card col-md-8 text-white">
        <img class="card-img feature-card-img" src="{{ post.image.url }}" alt="{{ post.title }}">
        <div class="card-img-overlay">
            <h5 class="card-title featured-card-title m-0">{{post.title}}</h5>
            <p class="card-text featured-card-text m-0">{{post.content|truncatechars:150}}.</p>
            <div class="showthis my-2">
                By: {{post.author}}
            </div>
        </div>  
    </a>
    
    {% endif %}
    {% endfor %}

    <div class="col-md-4 feature-info-box flexed">
        {% for post in posts  %}
        {% if post.small_feature == True %}
        <a href="{{post.get_absolute_url}}" class="main-feature-card-2 flexed">
            <img class="card-img small-feature-card-img" style="height: auto;" src="{{ post.image.url }}"
                alt="{{ post.title }}">
            <div class="card-img-overlay">
                <h5 class="card-title featured-card-title m-0">{{post.title}}</h5>
                <p class="card-text featured-card-text m-0"><em>{{post.excerpt}}.</em></p>
                <div class="showthis my-2">
                    By: {{post.author}}
                </div>
            </div>
        </a>
        {% endif %}
        {% endfor %}
    </div>



</div>
