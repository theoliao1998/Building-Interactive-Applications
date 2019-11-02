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
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"dj4e_hello.md","extra":"","action":false,"parameters":[],"current":"\/assn\/dj4e_hello.md","full":"\/assn\/dj4e_hello.md"},
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
  <option value="paw_home.md">Django Home Page</option>
  <option value="paw_details.md">Django Detail Pages</option>
  <option value="paw_sessions.md">Django Sessions</option>
  <option value="paw_users.md">Django Users</option>
  <option value="paw_forms.md">Django Forms</option>
  <option value="paw_github.md">Using GitHub</option>
  <option value="dj_install.md">Installing Django Locally</option>
  <option value="dj4e_hello.md" selected>Hello World</option>
  <option value="dj4e_autos.md">Autos CRUD</option>
  <option value="dj4e_ads1.md">AdList Milestone #1</option>
  <option value="dj4e_ads2.md">AdList Milestone #2</option>
  <option value="dj4e_ads3.md">AdList Milestone #3</option>
  <option value="dj4e_ads4.md">AdList Milestone #4</option>
</select>
</div>
<h1>DIY: Hello World</h1>
<p>At this point in the course we are going to start over and build a series of
applications in a Django project.  To review terminology, in the work that you
have done so far:</p>
<ul>
<li>
<p><code>django_projects</code> is a folder and/or a github repository that contains multiple
Django projects</p>
</li>
<li>
<p><code>locallibrary</code> is a <em>project</em> in that folder that can contain many applications.  The
project configuration is in the folder <code>localllibrary/locallibrary</code>.</p>
</li>
<li><code>catalog</code> is an <em>application</em> within the <code>locallibrary</code> project that has models,
views, templates, admin configurations, etc.</li>
</ul>
<p>We first need to make a new project within our <code>django_projects</code> folder.   It is time
to finish and then stop working on the <code>locallibrary</code> project.
Just keep it working so you can refer back to it as you build new applications.</p>
<h2>Making a New Project and Application</h2>
<p>Start a shell with virtual environment (if needed) and go into your <code>django_projects</code> folder
and start a new project and an application:</p>
<pre><code>workon django2                  # as needed
cd ~/django_projects
django-admin startproject dj4e

cd ~/django_projects/dj4e
python3 manage.py startapp home</code></pre>
<h2>Starting Django in the new project (local computer)</h2>
<pre><code>cd ~/django_projects/dj4e
python3 manage.py runserver</code></pre>
<p>In general as you make changes to the files below, runserver will monitor
for file changes and restart itself although sometimes you do want to abort
runserver and restart it manually to make sure it sees every new change.</p>
<h2>Switching to the new project (on PythonAnywhere)</h2>
<p>Under your Web tab, Set the following:</p>
<pre><code>Source Code:   /home/drchuck/django_projects/dj4e
Working Directory:   /home/drchuck/django_projects/dj4e</code></pre>
<p>The virtual environment should be pointing to your <code>django2</code> virtual environment:</p>
<pre><code>/home/drchuck/.virtualenvs/django2</code></pre>
<p>Replace <code>drchuck</code> above with your PythonAnywhere account name.</p>
<p>Your WGSI Configuration file under the Web tab on PythonAnywhere
should be replaced with this text:</p>
<pre><code>import os
import sys

path = os.path.expanduser('~/django_projects/dj4e')
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'dj4e.settings'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())</code></pre>
<p>Of course once you make these changes and other chenges below,
you need to Reload your application.</p>
<h2>Files to Edit/Create</h2>
<p>These are the steps to build your &quot;Hello World&quot; application.</p>
<ul>
<li>
<p>Make folders <code>django_projects/dj4e/home/templates</code> and <code>django_projects/dj4e/home/templates/home/</code></p>
</li>
<li>
<p>Create <code>django_projects/dj4e/home/templates/home/hello.html</code> and put in some text that says &quot;Hello World ... &quot; and
some additional text about cats and/or any text or meta tag
that the autograder is asking for.</p>
</li>
<li>
<p>Create the <code>django_projects/dj4e/home/urls.py</code> file to add a path that routes the '' path to a direct template view
pointing at a file <code>django_projects/dj4e/home/templates/home/hello.html</code> making sure to import <code>TemplateView</code> in the top
of the file:</p>
<pre><code>from django.urls import path
from django.views.generic import TemplateView

app_name='home'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home/hello.html'), name='home'),
]   </code></pre>
</li>
<li>
<p>Edit the <code>django_projects/dj4e/dj4e/settings.py</code>, make sure <code>DEBUG</code> is set to True, fix <code>ALLOWED_HOSTS</code> and add the home
application to <code>INSTALLED_APPS</code>:</p>
<pre><code>DEBUG = True                   # Make sure we see tracebacks in the UI

ALLOWED_HOSTS = [ '*' ]        # Allow access from anywhere

INSTALLED_APPS = [
    ...
    'home.apps.HomeConfig',    #  Add this
]</code></pre>
</li>
<li>
<p>Edit <code>django_projects/dj4e/dj4e/urls.py</code> to include the <code>django_projects/dj4e/home/urls.py</code> file.  Do <em>not</em> add any redirect
route like we used in the locallibrary / catalog application.  It should look like the following</p>
<pre><code>from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
]</code></pre>
</li>
</ul><script src="https://static.tsugi.org/js/jquery-1.11.3.js"></script>
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
