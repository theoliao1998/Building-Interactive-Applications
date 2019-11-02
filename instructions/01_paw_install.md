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
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"paw_install.md","extra":"","action":false,"parameters":[],"current":"\/assn\/paw_install.md","full":"\/assn\/paw_install.md"},
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
  <option value="paw_install.md" selected>Django and PythonAnywhere</option>
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
  <option value="dj4e_ads3.md">AdList Milestone #3</option>
  <option value="dj4e_ads4.md">AdList Milestone #4</option>
</select>
</div>
<h1>Installing Django on PythonAnywhere</h1>
<p>Before you start this assignment, you should already have signed up for a
<a href="https://www.pythonanywhere.com" target="_blank">PythonAnywhere</a>
account and be logged in on your account.  You should be able to complete all
of the exercises in this course using a free PythonAnywhere account.</p>
<p>This is a set of instructions to go through the first step of the
Mozilla Developer Network (MDN) Django tutorial to get
Django intalled on your PythonAnywhere account.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment">https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment</a></p>
<p>This is adapted from the PYAW documentation for following the Django tutorial.</p>
<p><a href="https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial/">https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial/</a></p>
<p>Feel free to look at that page as well.</p>
<p>You can view a
<a href="https://www.youtube.com/watch?v=lPpIubhqWR4&index=2&list=PLlRFEj9H3Oj5e-EH0t3kXrcdygrL9-u-Z" target="_blank">video walkthrough</a> of this assignment.</p>
<p>You can do all of the assignments on your local computer instead
of PythonAnywhere.  You will need to use the
<a href="../ngrok">ngrok</a> application
to submit your assignments to the autograder.</p>
<p><strong>Note:</strong> If you are submitting these assignments to the auto grader you
should complete each assignment and then submit it and get full credit before
moving on to the next assignment.  Because the assignments build on one another the application that you have build by the last step of the tutorial
will no longer pass the earlier autograders.</p>
<h2>Instructions</h2>
<p>Once you have created your PYAW account, start a <code>bash</code> shell
and set up a virtual environment with Python 3.x and Django 2.</p>
<pre><code>mkvirtualenv django2 --python=/usr/bin/python3.6
pip3 install django ## this may take a couple of minutes</code></pre>
<p>Note if you exit and re-start a new shell on PythonAnywhere - you need the following command
to get back into your virtual environment in the new bash shell.</p>
<pre><code>workon django2</code></pre>
<p>Lets make sure that your django was installed successfully with the following command:</p>
<pre><code>python3 -m django --version
# This should show something like 2.1.4</code></pre>
<p>Lets also get a copy of the sample code for DJ4E checked out so you can look at sample code
as the course progresses and install some important additional Django software libraries using
<code>pip3</code>.</p>
<pre><code>cd ~
git clone https://github.com/csev/dj4e-samples
cd dj4e-samples
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate</code></pre>
<p>In the PYAW shell, continue the steps from the MDN:</p>
<pre><code>cd ~
mkdir django_projects
cd django_projects
django-admin startproject mytestsite</code></pre>
<p>In the PYAW web interface navigate to the <code>Web</code> tab to create a new web application.  If you
have not already done so, add a new web application.  Select <code>manual configuration</code> and Python
3.6.  Once the webapp is created, you need to make a few changes to the settings for the web
app and your application.</p>
<pre><code>Source code: /home/drchuck/django_projects/mytestsite
Working directory: /home/drchuck/django_projects/mytestsite

Virtualenv: /home/drchuck/.virtualenvs/django2</code></pre>
<p>Replace <code>drchuck</code> with your account on PythonAnywhere.</p>
<p>Note that once you have your Virtualenv set up you have a very convenient link
titled &quot;Start a console in this virtualenv&quot; - this is a great way to open up consoles
so you never have to type &quot;workon django2&quot; and it makes sure your virtual
envronment is properly set up and configured.
<a href="paw_install/web_tab.png" target="_blank">Sample image</a></p>
<p>Then edit the <em>WGSI Configuration File</em> and put the following code into it.
Make sure to delete the existing contenxt of the file and replace it with the text below.
This is slightly different from the sample in the PythonAnywhere tutorial.</p>
<pre><code>import os
import sys

path = os.path.expanduser('~/django_projects/mytestsite')
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mytestsite.settings'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())</code></pre>
<p>You need to edit the file <code>~/django_projects/mytestsite/mytestsite/settings.py</code> and change
the allowed hosts line (around line 28) to be:</p>
<pre><code> ALLOWED_HOSTS = [ '*' ]</code></pre>
<p>There are three ways to edit files in your PythonAnywhere environment, ranging from the easiest
to the coolest.  You only have to edit the file one of these ways.</p>
<p>(1) Go to the main PythonAnywhere dashboard, browse files, navigate to the correct folder and edit the file</p>
<pre><code>/home/mdntutorial/django_projects/mytestsite/mytestsite/settings.py</code></pre>
<p>(2) Or in the command line:</p>
<pre><code>cd ~/django_projects/mytestsite/mytestsite/
nano settings.py

Save the File by pressing 'CTRL-X', 'Y', and Enter</code></pre>
<p>(3) Don't try this most difficult and most cool way to edit files on Linux without a helper
if it is your first time with the <code>vi</code> text editor.</p>
<pre><code>cd ~/django_projects/mytestsite/mytestsite/
vi settings.py</code></pre>
<p>Once you have opened <code>vi</code>, cursor down to the <code>ALLOWED_HOSTS</code> line,
position your cursor between the braces and press the
<code>i</code> key to go into 'INSERT' mode, then type your new text and press the <code>esc</code> key when you are
done.  To save the file, you type <code>:wq</code> followed by <code>enter</code>.  If you get lost press <code>escape</code> <code>:q!</code>
<code>enter</code> to get out of the file without saving.</p>
<p>If you aleady know some <em>other</em> command line text editor in Linux, you can use it to edit files.  In general,
you will find that it often quicker and easier to make small edits to files in the command line
rather than a full screen UI.  And once you start deploying real applications in production
environments like Google, Amazon, Microsoft, etc.. all you will have is command line.</p>
<p>Once this file has been edited, on the PYAW Web tab, <code>Reload</code> your web application, wait a few seconds and check
that it is up and running:</p>
<pre><code>http://drchuck.pythonanywhere.com/</code></pre>
<p>Replace <code>drchuck</code> with your account on PythonAnywhere.</p>
<p>Here is a
<a href="paw_install/index.htm" target="_blank">Sample</a>
of what the resulting page should look like.</p><script src="https://static.tsugi.org/js/jquery-1.11.3.js"></script>
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
