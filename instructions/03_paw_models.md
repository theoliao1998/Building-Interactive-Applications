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
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"paw_models.md","extra":"","action":false,"parameters":[],"current":"\/assn\/paw_models.md","full":"\/assn\/paw_models.md"},
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
  <option value="paw_models.md" selected>Django Models</option>
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
<h1>Django Models</h1>
<p>Our next step is to add some models to our LocalLibrary application so we can store
data in our database.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models">https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models</a></p>
<p>You can view a
<a href="https://www.youtube.com/watch?v=2-QFePlm7GA&list=PLlRFEj9H3Oj5e-EH0t3kXrcdygrL9-u-Z&index=5" target="_blank">video walkthrough</a> of this assignment.</p>
<p>Read and understand the tutorial, and when you get to the section titled
<a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models#Defining_the_LocalLibrary_Models" target="_blank">Defining the LocalLibrary Models</a>,
go to your
<a href="https://www.pythonanywhere.com" target="_blank">PythonAnywhere</a>
account and start a bash shell.</p>
<p>Lets go into the locallibrary project:</p>
<pre><code>workon django2
cd ~/django_projects/locallibrary</code></pre>
<p>Make sure that you have properly edited the <code>locallibrary/settings.py</code> file to register your catalog
application within the locallibrary project by adding <code>CatalogConfig</code> line:</p>
<pre><code>ALLOWED_HOSTS = ['*']   &lt;-- Change

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',             # Add this line
    'catalog.apps.CatalogConfig',    # Add this line
]</code></pre>
<p>Edit the file <code>catalog/models.py</code> and add the <code>Genre</code> model using as described in the tutorial.
You can edit the file with <code>nano</code>, <code>vi</code>, or the PythonAnywhere Files tab interface.  Once you have added
the model, run the migrations from <code>~/django_projects/locallibrary</code></p>
<pre><code>python3 manage.py makemigrations
python3 manage.py migrate</code></pre>
<p>If you are using <code>git</code>, you can see what files have been modified / created:</p>
<pre><code>git status</code></pre>
<p>The git output would be as follows:</p>
<pre><code>modified:   catalog/models.py
Untracked files:
    catalog/migrations/0001_initial.py   </code></pre>
<p>The <code>git</code> command won't show the <code>db.sqlite3</code> file has changed because we have told <code>git</code>
not to track the database file in the <code>.gitignore</code> file</p>
<p>Lets take a quick look at the contents of the <code>db.sqlite3</code> file in your bash shell:</p>
<pre><code>$ sqlite3 db.sqlite3 
SQLite version 3.11.0 2016-02-15 17:29:24
Enter ".help" for usage hints.
sqlite&gt; .tables
auth_group                  catalog_genre
auth_group_permissions      django_admin_log
auth_permission             django_content_type
auth_user                   django_migrations
auth_user_groups            django_session
auth_user_user_permissions
sqlite&gt; .mode column
sqlite&gt; select * from catalog_genre;
sqlite&gt; .schema catalog_genre
CREATE TABLE "catalog_genre" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "name" varchar(200) NOT NULL);
sqlite&gt; .quit  </code></pre>
<p>You can learn more about the command line mode of <code>sqlite3</code> at their web site:</p>
<p><a href="https://www.sqlite.org/cli.html">https://www.sqlite.org/cli.html</a></p>
<p>Continue editing the <code>catalog/models.py</code> file and add the Book, BookInstance, and Author models
according to the tutorial.</p>
<p>Also add the <code>language</code> field to the correct table as discussed in the &quot;Challenge&quot; section
at the end of the tutorial.</p>
<p>Once your models.py file is complete, run the migrations again:</p>
<pre><code>cd ~/django_projects/locallibrary
python3 manage.py makemigrations
python3 manage.py migrate</code></pre>
<p>You can repeat the process of editing the <code>models.py</code> file and re-running the migrations until you get them
right.</p>
<p>If you are using the autograder for this assignment, you will need to upload the
<code>db.sqlite3</code> file.  If you are using PythonAnywhere you can use the Files tab
to download the file to your computer and then upload it to the autograder.</p><script src="https://static.tsugi.org/js/jquery-1.11.3.js"></script>
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
