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
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"paw_github.md","extra":"","action":false,"parameters":[],"current":"\/assn\/paw_github.md","full":"\/assn\/paw_github.md"},
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
  <option value="paw_github.md" selected>Using GitHub</option>
  <option value="dj_install.md">Installing Django Locally</option>
  <option value="dj4e_hello.md">Hello World</option>
  <option value="dj4e_autos.md">Autos CRUD</option>
  <option value="dj4e_ads1.md">AdList Milestone #1</option>
  <option value="dj4e_ads2.md">AdList Milestone #2</option>
  <option value="dj4e_ads3.md">AdList Milestone #3</option>
  <option value="dj4e_ads4.md">AdList Milestone #4</option>
</select>
</div>
<h1>Storing your Django Projects in GitHub</h1>
<p>This excercise shows how to store your assignments in a private repository in
<a href="https://www.github.com" target="_blank">GitHub</a>,
if you have an account that supports a private repository.  Please don't put your
assignments for this site into a public repository on GitHub.</p>
<p>You can view a
<a href="https://www.youtube.com/watch?v=9FJwue2Eqao&list=PLlRFEj9H3Oj5e-EH0t3kXrcdygrL9-u-Z&index=2" target="_blank">video walkthrough</a> of this assignment.</p>
<p>Go to GitHub, create a new private repo called <code>django_projects</code> - do not create
a README, .gitignore, or add a license.  You can do those things later - but for now
we want to make a new fresh and <em>empty</em> repository.</p>
<p>Go to your
<a href="https://www.pythonanywhere.com" target="_blank">PythonAnywhere</a>
account and start a bash shell.</p>
<p>Create a file</p>
<pre><code>cd ~/django_projects
nano .gitignore</code></pre>
<p>Put these three lines into the file and save it.</p>
<pre><code>__pycache__
*.swp
*.sqlite3</code></pre>
<p>Remember that to see all the files in a folder (including those that start with a '.')
you need to type <code>ls -la</code>.</p>
<p>Still in your PythnonAnywhere shell in the <code>~/django_projects</code> folder, run
the following commands:</p>
<pre><code>git init
git config --global push.default simple
git add *
git add .gitignore
git status
git config --global user.email "youremail@umich.edu"
git config --global user.name "Your X. Name"
git config --global credential.helper cache   # Optional but convienent
git config --global credential.helper 'cache --timeout=604800'  # Optional but convienent
git commit -m "first commit" 
git remote add origin https://github.com/--your-github-acct--/django_projects.git
git push -u origin master
(enter id and password for git)</code></pre>
<p>Go to </p>
<pre><code>https://github.com/--your-github-account---/django_projects</code></pre>
<p>Verify the data has been pushed to the repo and verify that it is private.</p>
<p>If you get tired of typing your github credentials over and over, you can tell
the bash shell to cache them for a week using the following commands:</p>
<h2>Local and Remote Repositories Out of Sync</h2>
<p>Sometimes when you have a repo and are working on files, and start typing
things like <code>git commit -a</code> or <code>git push</code> you start getting very strange
errors start appearing that imply that you can't do what you are trying to
do.</p>
<p>Often this is because you are doing things in your repo two different
places (i.e. your laptop and PythonAnywhere) and one or the other copies is
out of sync with the copy that you have stored in GitHub.</p>
<p>When your remote repository is &quot;ahead&quot; of your local repository, you
will see the following error when you do a <code>git pull</code>:</p>
<pre><code>$ git status
On branch master

    modified:   locallibrary/settings.py

$ git pull
error: cannot pull with rebase: You have unstaged changes.
error: please commit or stash them.</code></pre>
<p>Solving this is pretty simple, the following sequence will work:</p>
<pre><code>git stash
git pull
git stash apply</code></pre>
<p>This undoes your local changes (except for added files whch don't
affect the pull) but &quot;stashes&quot; them.
Then the pull will work and the <code>git stash apply</code> retrieves your &quot;stashed&quot;
changes and re-applies them.  </p>
<h2>Harder to Fix Problems</h2>
<p>If you end up in a situation where git is complaining about a &quot;merge conflict&quot;
you can Google around and find a solution.  But sometimes that is
kind of obtuse and it is easier to grab a fresh copy of your repo
and manually re-apply your changes.</p>
<p>If things are really messed up and <code>git</code> is complaining about a lock file,
or something else very mysterious, sometimes the quickest
way to get going again is to take a step back
and then go forward again.  This process assumes that you have something in
github to go back to.  </p>
<p>Here are the steps to restore your <code>django_projects</code> folder.  You may
lose a few bits in this process but your git folder will work again.</p>
<p>First lets see what changes we have made because we will need to redo
the changes.</p>
<pre><code>cd ~/django_projects
git status</code></pre>
<p>Then rename your folder and check out a fresh copy of your repository:</p>
<pre><code>cd ~
mv django_projects broken_version
git clone https://github.com/drchuck/django_projects.git</code></pre>
<p>Replacing <code>drchuck</code> with your github account.</p>
<p>Now you have a fresh new copy of your github repository.  Then go into
the saved copy and see which files you want to copy over into the newly
checked out copy of your repo:</p>
<pre><code>cd ~/broken_version
git status</code></pre>
<p>Then for each file you want to put back into your freshly checked out repo, do:</p>
<pre><code>cp locallibrary/locallibrary/settings.py ../django_projects/locallibrary/locallibrary/settings.py</code></pre>
<p>You can also use the Linux <code>diff</code> command to see how files differ before making
the copy:</p>
<pre><code>diff locallibrary/locallibrary/settings.py ../django_projects/locallibrary/locallibrary/settings.py</code></pre>
<p>Use tab completion to make sure that you are typing folders and files
correctly.</p>
<p>If you are dealing with a merge conflict, you may still need to go into the
newly checked out folder and edit the files before committing.  The git
merge process puts little marks in the file to show where the conflicts
were found.  Just test your code before committing and uploading - any merge
lines in the file will be syntax errors in your application that you can
fix.</p>
<p>You can change the folder paths from this example depending on
what repo you are working with and where in your folder structure
you are working.</p>
<h2>References</h2>
<p><a href="https://help.github.com/articles/caching-your-github-password-in-git/#platform-linux">https://help.github.com/articles/caching-your-github-password-in-git/#platform-linux</a></p><script src="https://static.tsugi.org/js/jquery-1.11.3.js"></script>
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
