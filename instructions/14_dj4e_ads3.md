<!DOCTYPE html>
    <html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DJ4E - Django for Everybody</title>
        <script>
        var _TSUGI = {
            ajax_session: false,
            heartbeat: 1500000,
            heartbeat_url: "https://www.dj4e.com/tsugi/util/heartbeat?msec=1500000",
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"dj4e_ads3.md","extra":"","action":false,"parameters":[],"current":"\/assn\/dj4e_ads3.md","full":"\/assn\/dj4e_ads3.md"},
            spinnerUrl: "https://static.tsugi.org/img/spinner.gif",
            staticroot: "https://static.tsugi.org",
            websocket_url: false,
            websocket_token: false,
            window_close_message: "Application complete",
            session_expire_message: "Your session has expired"
        }
        </script>
        <!-- Tiny bit of JS -->
        <script src="https://static.tsugi.org/js/tsugiscripts_head.js"></script>
        <!-- Le styles -->
        <link href="https://static.tsugi.org/bootstrap-3.4.1/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://static.tsugi.org/js/jquery-ui-1.11.4/jquery-ui.min.css" rel="stylesheet">
                <link href="https://static.tsugi.org/fontawesome-free-5.8.2-web/css/all.css" rel="stylesheet">
        <link href="https://static.tsugi.org/fontawesome-free-5.8.2-web/css/v4-shims.css" rel="stylesheet">
        <style>:root {--primary:#0D47A1;--primary-border:#0d4295;--primary-darker:#0c4091;--primary-darkest:#0b3b85;--secondary:#EEEEEE;--text:#111111;--text-light:#5E5E5E;--font-family:sans-serif;--font-size:14px;}</style>
          <link href="https://static.tsugi.org/css/tsugi.css" rel="stylesheet">

          <style>
                        </style>
<style>
a[target="_blank"]:after {
    font-family: 'Font Awesome 5 Free';
    font-weight: 600;
    content: " \f35d";
}
.goog-te-banner-frame.skiptranslate {
    display: none !important;
    }
body {
    top: 0px !important;
    }
</style>

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="https://www.dj4e.com/tsugi/vendor/tsugi/lib/static/js/html5shiv/html5shiv.js"></script>
          <script src="https://www.dj4e.com/tsugi/vendor/tsugi/lib/static/js/respond/respond.min.js"></script>
        <![endif]-->

    <script type="text/javascript">CSRF_TOKEN = "TODORemoveThis";</script>
</head>
<body prefix="oer: http://oerschema.org">
<div id="body_container">
<script>
if (window!=window.top) {
    document.getElementById("body_container").className = "container-fluid";
} else {
    document.getElementById("body_container").className = "container";
}
</script>
<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation" id="tsugi_main_nav_bar" style="display:none">  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="https://www.dj4e.com">DJ4E</a>
    </div>
    <div class="navbar-collapse collapse">
      <ul class="nav navbar-nav navbar-main">
        <li><a href="https://www.dj4e.com/lessons" >Lessons</a></li>
        <li><a href="https://www.dj4e.com/assn" >Assignments</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="http://www.dr-chuck.com" target="_blank" >Instructor</a></li>
        <li><a href="https://www.dj4e.com/tsugi/login.php" >Login</a></li>
      </ul>
    </div> <!--/.nav-collapse -->
  </div> <!--container -->
</nav>
<script>
if ( ! inIframe() ) {
  document.getElementById('tsugi_main_nav_bar').style.display = 'block';
  document.getElementsByTagName('body')[0].style.paddingTop = '5.93rem';
}
</script>
<div id="flashmessages"></div><style>
center {
    padding-bottom: 10px;
}
@media print {
    #chapters {
        display: none;
    }
}
a[target="_blank"]:after {
  content: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAQElEQVR42qXKwQkAIAxDUUdxtO6/RBQkQZvSi8I/pL4BoGw/XPkh4XigPmsUgh0626AjRsgxHTkUThsG2T/sIlzdTsp52kSS1wAAAABJRU5ErkJggg==);
  margin: 0 3px 0 5px;
}
</style>
</head>
<body prefix="oer: http://oerschema.org">
<div id="body_container">
<script>
if (window!=window.top) {
    document.getElementById("body_container").className = "container-fluid";
} else {
    document.getElementById("body_container").className = "container";
}
</script>
<script>
function onSelect() {
    console.log($('#chapters').val());
    window.location = $('#chapters').val();
}
</script>
<div style="float:right">
<select id="chapters" onchange="onSelect();">
  <option value="paw_install.md">Django and PythonAnywhere</option>
  <option value="paw_skeleton.md">Skeleton web site</option>
  <option value="paw_models.md">Django Models</option>
  <option value="paw_admin.md">Django Admin</option>
  <option value="dj4e_load.md">Batch Loading Data</option>
  <option value="paw_home.md">Django Home Page</option>
  <option value="paw_details.md">Django Detail Pages</option>
  <option value="paw_sessions.md">Django Sessions</option>
  <option value="paw_users.md">Django Users</option>
  <option value="paw_forms.md">Django Forms</option>
  <option value="paw_github.md">Using GitHub</option>
  <option value="dj_install.md">Installing Django Locally</option>
  <option value="dj4e_hello.md">Hello World</option>
  <option value="dj4e_autos.md">Autos CRUD</option>
  <option value="dj4e_ads1.md">AdList Milestone #1</option>
  <option value="dj4e_ads2.md">AdList Milestone #2</option>
  <option value="dj4e_ads3.md" selected>AdList Milestone #3</option>
  <option value="dj4e_ads4.md">AdList Milestone #4</option>
</select>
</div>
<h1>Classified Ad Web Site - Milestone 3</h1>
<p>In this assignment, you will expand your classified ads web site to add functionality
equivalent to:</p>
<p><a href="https://chucklist.dj4e.com/m3">https://chucklist.dj4e.com/m3</a></p>
<p>We will add a favoriting capability to your previous milestone by borrowing more parts and pieces from the code that runs:</p>
<p><a href="https://samples.dj4e.com/">https://samples.dj4e.com/</a></p>
<h2>Do All of the Challenges</h2>
<p>At this point all of the challenges should be working - not all will be tested
by the autograder - but we will separately check them.</p>
<p>(1) Make yourself a gravatar at <a href="https://en.gravatar.com/">https://en.gravatar.com/</a> - it is super easy and you will see your
avatar when you log in in your application and elsewhere with gravatar enabled apps. The gravatar can be
any thing you like - it does not have to be a picture of you.</p>
<p>(2) Change your <code>home/static/favicon.ico</code> to a favicon of your own making.   I made my favicon
at <a href="https://favicon.io/favicon-generator/">https://favicon.io/favicon-generator/</a> - it might not change instantly after you update the favicon
because they are cached extensively.   Probably the best way to test is to go right to the favicon url
after up update the file and press 'Refresh' and.or switch browsers.</p>
<p>(3) Make social login work.  Take a look at
<a href="https://github.com/csev/dj4e-samples/blob/master/dj4e-samples/github_settings-dist.py" target="_blank">
github_settings-dist.py</a>, copy it into
<code>adlist/adlist/github_settings.py</code> and go through the process on github to get your client ID and
secret.   The documentation is in comments of the file.  Also take a look at
<a href="https://github.com/csev/dj4e-samples/blob/master/dj4e-samples/urls.py" target="_blank">
dj4e-samples/urls.py</a> and make sure that the &quot;Switch to social login&quot; code is correct
and at the end of your <code>adlist/adlist/github_settings.py</code>.</p>
<pre><code># The code below dynamically switches between non-social login.html 
# and social_login.html when we notice that social login has been
# configured in settings.py (later in the course)
# Or just uncomment the path above when you enable social login

from django.contrib.auth import views as auth_views
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
        path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
    )
    print('Using',social_login,'as the login template')
except:
    print('Using registration/login.html as the login template')</code></pre>
<p>You can register two applications with github - one on localhost and one on PythonAnywhere.  If you are
using github login on localhost - make sure that you register <code>http://127.0.0.1:8000/</code> instead
of <code>http://localhost:8000/</code> and use that in your browser to test your site.  If you
use localhost, you probably will get the <code>The redirect_uri MUST match the registered callback URL for this application.</code> error message when you use social login.</p>
<h2>Adding Favorites to the Ads Application</h2>
<p>In this section, you will pull bits and pieces of the <code>favs</code> sample application
into your <code>ads</code> application to add support for logged in users to &quot;favorite&quot; and &quot;un-favorite&quot;
ads.</p>
<p>(1) Add this to your <code>ads/model.py</code>, talking inspiration from <code>dj4e-samples/favs/models.py</code></p>
<pre><code>class Ad(models.Model) :

    ...

    # Favorites
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL,
        through='Fav', related_name='favorite_ads')
    ...

class Fav(models.Model) :
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # https://docs.djangoproject.com/en/2.1/ref/models/options/#unique-together
    class Meta:
        unique_together = ('ad', 'user')

    def __str__(self) :
        return '%s likes %s'%(self.user.username, self.ad.title[:10])</code></pre>
<p>Of course do the migrations once you have modified the model.</p>
<p>(2) Add two routes to your <code>urls.py</code> for the favorite features</p>
<pre><code>...
path('ad/&lt;int:pk&gt;/favorite',
    views.AddFavoriteView.as_view(), name='ad_favorite'),
path('ad/&lt;int:pk&gt;/unfavorite',
    views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
...</code></pre>
<p>(3) Look at how <code>ThingListView</code> from <code>dj4e-samples/favs/views.py</code>
retrieves the list of favorites for the current user and add code
to your <code>AdListView</code> to retrieve the favorites for the current logged in user.</p>
<p>(4) Alter your <code>ad_list.html</code> by looking through <code>favs/templates/favs/list.html</code>.  Make sure to add the
parts that show the stars based on the list of favorites for this user and the <code>favPost()</code> JavaScript
code at the end.</p>
<p>(5) Pull in and adapt <code>AddFavoriteView</code>, and <code>DeleteFavoriteView</code>
from <code>dj4e-samples/favs/views.py</code> into your <code>views.py</code>.</p>
<h2>Manual Testing</h2>
<p>It is always a good idea to manually test your application before submitting it for grading.  Here
are a set of manual test steps:</p>
<ul>
<li>Make two accounts</li>
<li>Log in to your application on the first account</li>
<li>Create an ad, view its details, update, the ad, and delete the ad (test for regression)</li>
<li>Create more than one ad</li>
<li>In the list view mark one ad as a favorite and then press 'refresh' and see if the star is the same
after refresh as it was when you clicked on the star</li>
<li>In the list view unfavorite a favorited ad and then press 'refresh' and see if the star is the same
after refresh as it was when you clicked on the star</li>
<li>Log in on the second account - make sure the favorites are not the same as the first account</li>
<li>Do several favorite and unfavorite operations pressing 'refresh' after each change and make sure
the star &quot;sticks&quot; (i.e. has the same value as when you clicked it)</li>
</ul>
<p>The most common problem is that when you click onthe star if looks good on the screen but the
fact that this is not a favorites (or not) did not get recorded in the server.<br />
Often you will need to check the developer network console in your browser to find errors
in the AJAX code.</p><script src="https://static.tsugi.org/js/jquery-1.11.3.js"></script>
<script src="https://static.tsugi.org/bootstrap-3.4.1/js/bootstrap.min.js"></script>
<script src="https://static.tsugi.org/js/jquery-ui-1.11.4/jquery-ui.min.js"></script>
<script src="https://static.tsugi.org/js/jquery.timeago-1.6.3.js"></script>
<script src="https://static.tsugi.org/js/handlebars-v4.0.2.js"></script>
<script src="https://static.tsugi.org/tmpljs-3.8.0/tmpl.min.js"></script>
<script src="https://static.tsugi.org/js/tsugiscripts.js"></script>
<script type="text/javascript">
    HEARTBEAT_TIMEOUT = setTimeout(doHeartBeat, _TSUGI.heartbeat);
    tsugiEmbedMenu();
</script>
<div id="google_translate_element" style="position: fixed; right: 1em; bottom: 0.25em;"></div><script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: "en", layout: google.translate.TranslateElement.InlineLayout.SIMPLE
    }, "google_translate_element");
}
</script><script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
<script>
// PHP VERSION 7.0 and 7.1 HACK
// https://stackoverflow.com/questions/44980654/how-can-i-make-trans-sid-cookie-less-sessions-work-in-php-7-1
$('a').each(function (x) {
    var href = $(this).attr('href');
    if ( ! href ) return;
    if ( ! href.startsWith('#') ) return;
    var pos = href.indexOf('/?');
    if ( pos < 1 ) return;
    console.dir('Patching broken # href='+href);
    href = href.substring(0,pos);
    $(this).attr('href', href);
});

</script>
<script>
// https://stackoverflow.com/questions/7901679/jquery-add-target-blank-for-outgoing-link
$(window).load(function() {
    $('a[href^="http"]').attr('target', function() {
      if(this.host == location.host) return '_self'
      else return '_blank'
    });
});
</script>

</div></body>
</html>
