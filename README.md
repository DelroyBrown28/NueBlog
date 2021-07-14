LARGE FEATURE:

<div class="album py-5">
    <div class="container">
        <div class="row">
            {% for post in posts %}
            {% if post.large_feature == True %}

            <div class="col-md-7">
                <a class="text-dark" href="{{post.get_absolute_url}}">
                    <div class="featured-card mb-5">
                        <div class="large-feature-overlay flexed">

                            <div class="featured-card-body">
                                <h2 style="font-size:18px;font-weight:bold;color: white;">
                                    {{post.title|truncatechars:50}}</h2>
                                <p class="card-text" style="height: 65px;">By: {{post.author}}</p>
                                <div class="socials row">
                                    {% post_to_facebook object_or_url "<i style='color: #FFF    ' class='fab fa-facebook-f'></i>" %}
                                    {% post_to_twitter "Check out this post by {{ post.author }}, called {{ post.title }}" object_or_url "<i style='color: #FFF' class='fab fa-twitter'></i>" %}
                                    <a style="cursor: pointer;" class="pinterest-this ">
                                        <span class="PIN_1626091531472_button_pin PIN_1626091531472_save"
                                            data-pin-log="button_pinit_bookmarklet"><i style='color: #FFF'
                                                class="fab fa-pinterest"></i></span>
                                    </a>
                                    {% post_to_reddit "Check out this post by {{ post.author }}, called {{ post.title }}" object_or_url "<i style='color: #FFF' class='fab fa-reddit'></i>" %}
                                    {% post_to_whatsapp  object_or_url "<i style='color: #FFF' class='fab fa-whatsapp'></i>" %}
                                </div>
                            </div>
                        </div>
                        <!-- <div class="d-flex py-1 justify-content-between align-items-right">
                            <small class="text-muted post-published-date">{{post.publish}}</small>
                            <small class="text-muted post-author">{{post.author}}</small>

                        </div> -->
                        <img class="featured-card-img-top img-fluid post-image" src="{{ post.image.url }}"
                            alt="{{ post.title }}">

                    </div>
                </a>

            </div>
            {% endif %}
            {% endfor %}

            <div class="col-md-5 small-featured-box flexed">
                <!-- <div class="col-md-5 logo-section flexed">
                    <h2 class="featured-title">LATESTS POSTS</h2>
                </div> -->
                {% for post in posts %}
                {% if post.small_feature_1 == True %}
                <a class="text-dark" href="{{post.get_absolute_url}}">
                    <div class="small-featured-card">
                        <!-- <div class="featured-card-body">
                            <h2 style="font-size:18px;font-weight:bold">{{post.title|truncatechars:50}}</h2>
                            <p class="card-text" style="height: 65px;">{{post.excerpt|truncatechars:50}}</p>
            
                        </div>
                        <div class="d-flex py-1 justify-content-between align-items-right">
                            <small class="text-muted post-published-date">{{post.publish}}</small>
                            <small class="text-muted post-author">{{post.author}}</small>
            
                        </div> -->
                            <img class="small-featured-card-img-top post-image" src="{{ post.image.url }}"
                                alt="{{ post.title }}">

                    </div>
                </a>
                {% endif %}
                {% endfor %}

            </div>
        </div>
    </div>
</div>
