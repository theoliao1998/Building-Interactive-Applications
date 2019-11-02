<!DOCTYPE html>
    <html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DJ4E - Django for Everybody</title>
        <script>
        var _TSUGI = {
            context_title: "SI 664 001 FA 2019",
            link_title: "Tool: Autograder: Request-Response Cycle",
            user_displayname: "Xinhao Liao",
            user_locale: "en",
            ajax_session: false,
            heartbeat: 1500000,
            heartbeat_url: "https://www.dj4e.com/tsugi/util/heartbeat?msec=1500000",
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"paw_home.md","extra":"","action":false,"parameters":[],"current":"\/assn\/paw_home.md","full":"\/assn\/paw_home.md"},
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

    <script type="text/javascript">CSRF_TOKEN = "5dbde64861f20";</script>
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
  <option value="paw_home.md" selected>Django Home Page</option>
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
  <option value="dj4e_ads3.md">AdList Milestone #3</option>
  <option value="dj4e_ads4.md">AdList Milestone #4</option>
</select>
</div>
<h1>Django Home Page</h1>
<p>Ironically, we are several steps into this tutorial and we <em>finally</em> get
to the point where we are building the elements of <em>our</em> user interface into
our application.  Most everything up to this point is book keeping.</p>
<p>Our next step is to add some url routes and views to
our LocalLibrary application so we can build some user interface bits.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page">https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page</a></p>
<p>If you are submitting this assignment to the DJ4E autograder
for this assignment,
it would be a good idea to check the autograder for specific instructions that
the autograder requires for this assignment.</p>
<p>Complete the following sections of the Views tutorial:</p>
<ul>
<li>
<p>Go into the <code>catalog</code> application</p>
<pre><code>cd ~/django_projects/locallibrary/catalog</code></pre>
</li>
<li>
<p>Edit <code>catalog/urls.py</code> so it looks like follows:</p>
<pre><code>from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),    # New line as per tutorial
]

# New lines below to serve static files in debug mode
import os
from django.urls import re_path
from django.views.static import serve
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns += [
    re_path(r'^static/(?P&lt;path&gt;.*)$', serve, {
        'document_root': os.path.join(BASE_DIR, 'catalog/static'),
    }),
]</code></pre>
<p>We need the extra bits to serve the static files locally in debug mode.  We will come back
to talk about how to serve static files when we move our application to production.</p>
</li>
<li>
<p>Edit <code>views.py</code> for the views.index as suggested in the tutorial</p>
</li>
<li>
<p>You will have to make the <code>templates</code> and <code>static</code> directories</p>
<pre><code>cd ~/django_projects/locallibrary/catalog
mkdir templates
mkdir static
mkdir static/css</code></pre>
</li>
<li>
<p>Create the file <code>templates/base_generic.html</code>as suggested.  The tutorial shows a simple version and then a more complex version with some CSS files - create the more complex version.  The autograder may require the addition of a <code>&lt;meta&gt;</code> tag in the <code>&lt;head&gt;</code> area of the base template.</p>
</li>
<li>
<p>Create the file <code>static/css/styles.css</code> as suggested</p>
</li>
<li>
<p>Create the file <code>templates/index.html</code>as suggested but replace the string &quot;Mozilla Developer Network!&quot; with something else.  You do not need to use your name if you don't want to - it just must be something other than the text in the tutorial.</p>
</li>
<li>
<p>Reload your application under the <code>Web</code> tab in
<a href="https://www.pythonanywhere.com" target="_blank">PythonAnywhere</a></p>
</li>
<li>Visit the catalog site
<a href="http://mdntutorial.pythonanywhere.com/catalog" target="_blank"><a href="http://mdntutorial.pythonanywhere.com/catalog">http://mdntutorial.pythonanywhere.com/catalog</a></a></li>
</ul>
<p>When you make changes to configuration files like <code>urls.py</code> or <code>views.py</code> it is always a good idea to reload
your web application on
<a href="https://www.pythonanywhere.com" target="_blank">PythonAnywhere</a>
under the <code>Web</code> tab and <code>Reload</code> the web server to re-read your updated configuration files.</p>
<p>Generally the server automatically detects changes to templates or static files
without requiring your application to be reloaded.  There is not harm in reloading your
web application too often.  If you made a change and dont think you are seeing the change,
reload the web application.</p>
<h2>Common Problems and How to Fix Them</h2>
<p>If you reload your web application and get the &quot;Something went wrong :(&quot;
page when you access your web application, check on the &quot;error.log&quot; link
and scroll to the very bottom to see why your application will not start.
If you see and error message like:</p>
<pre><code>No module named 'django_extensions'</code></pre>
<p>It probably means that you have not set up your virtual environment under
the <code>Web</code> tab.  </p>
<p>If you did the installation properly and created a <code>django2</code>
virtual environment, the virtual environment under the <code>Web</code> tab should be set to:</p>
<pre><code>/home/drchuck/.virtualenvs/django2</code></pre>
<p>Replacing &quot;drchuck&quot; with your PythonAnywhere account name.</p>
<h2>References</h2>
<p><a href="https://docs.djangoproject.com/en/2.1/ref/views/">https://docs.djangoproject.com/en/2.1/ref/views/</a></p>
<p><a href="https://stackoverflow.com/questions/30430131/get-the-file-path-for-a-static-file-in-django-code">https://stackoverflow.com/questions/30430131/get-the-file-path-for-a-static-file-in-django-code</a></p><script src="https://static.tsugi.org/js/jquery-1.11.3.js"></script>
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
