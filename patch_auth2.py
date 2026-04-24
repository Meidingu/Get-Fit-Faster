
import re

with open(r'C:\Users\ajaok\OneDrive\Desktop\FitnessApp\frontend\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print(f'File loaded, length: {len(html)}')

# =========================================================
# PART 1: Replace video background div + overlay
# =========================================================
# Find and replace the video bg section
vid_start = html.find('<!-- VIDEO BACKGROUND -->')
if vid_start == -1:
    vid_start = html.find('<!-- CINEMATIC HERO BACKGROUND -->')

spline_end_marker = '<div class="spline-overlay"></div>'
spline_end = html.find(spline_end_marker)

if vid_start != -1 and spline_end != -1:
    end_of_section = spline_end + len(spline_end_marker)
    new_bg = '  <!-- CINEMATIC HERO BACKGROUND -->\n  <div id="hero-bg">\n    <div class="hero-bg-gradient"></div>\n  </div>'
    html = html[:vid_start] + new_bg + html[end_of_section:]
    print('OK: Video section replaced')
else:
    print(f'SKIP: vid_start={vid_start}, spline_end={spline_end}')

# =========================================================
# PART 2: Replace auth-screen HTML
# =========================================================
auth_start_marker = '<div id="auth-screen">'
app_screen_marker = '<div id="app-screen">'

auth_start = html.find(auth_start_marker)
app_start = html.find(app_screen_marker)

if auth_start != -1 and app_start != -1:
    new_auth = '''  <div id="auth-screen">
    <!-- Cinematic typography layer -->
    <div class="hero-typography">
      <div class="hero-word hero-track">track</div>
      <div class="hero-slash-group">
        <span class="hero-slash">/</span><span class="hero-your">your</span>
      </div>
      <div class="hero-activity">activity</div>
    </div>

    <!-- Phone mockup card -->
    <div class="hero-phone">
      <div class="phone-card">
        <div class="phone-label">YOU RUN TODAY</div>
        <div class="phone-km">10.73 <span>KM</span></div>
        <div class="phone-map">
          <svg viewBox="0 0 160 120" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%">
            <polyline class="route-line" points="30,100 40,85 35,70 50,60 45,42 60,30 75,38 80,28 95,22 105,35 115,28 130,40 125,55 135,68 120,80 110,90 95,100 80,95 65,105 50,98 38,110" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
            <circle cx="30" cy="100" r="4" fill="#ff6600"/>
            <circle cx="130" cy="40" r="3" fill="white" opacity="0.6"/>
          </svg>
          <div class="map-location">SILICON<br>VALLEY</div>
        </div>
        <div class="phone-stats">
          <div class="phone-stat">
            <div class="phone-stat-label">PACE</div>
            <div class="phone-stat-val">3:23<span>/KM</span></div>
          </div>
          <div class="phone-stat">
            <div class="phone-stat-label">TIME</div>
            <div class="phone-stat-val">42:22</div>
          </div>
          <div class="phone-stat">
            <div class="phone-stat-label">ENERGY</div>
            <div class="phone-stat-val">135<span>KCAL</span></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom social row -->
    <div class="hero-social">
      <div class="hero-social-left">
        <span class="social-label">RUN WITH</span>
        <div class="social-avatars">
          <div class="avatar av1"></div>
          <div class="avatar av2"></div>
          <div class="avatar av3"></div>
        </div>
        <span class="social-label">FRIENDS</span>
      </div>
      <div class="hero-social-right">
        Running with friends can be a fantastic way to stay motivated and enjoy the outdoors.
      </div>
    </div>

    <!-- Floating login panel -->
    <div class="auth-panel">
      <div class="auth-panel-inner">
        <div class="auth-brand-mini">
          <span class="brand-dot"></span>
          <span class="brand-name">GET FIT FASTER</span>
        </div>
        <div class="auth-switch">
          <button class="auth-switch-btn active" onclick="authTab(\'login\')">Login</button>
          <button class="auth-switch-btn" onclick="authTab(\'register\')">Register</button>
        </div>
        <div id="form-login">
          <div class="auth-form-title">Welcome<br><em>back.</em></div>
          <div class="auth-form-sub">Enter your credentials to continue</div>
          <div class="auth-err" id="login-err"></div>
          <div class="field"><label class="field-label">Email address</label><input class="field-input" id="l-email" type="email" placeholder="you@email.com"></div>
          <div class="field"><label class="field-label">Password</label><input class="field-input" id="l-pass" type="password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;"></div>
          <button class="btn-volt" onclick="doLogin()">Start Running &rarr;</button>
        </div>
        <div id="form-register" style="display:none">
          <div class="auth-form-title">Join<br><em>today.</em></div>
          <div class="auth-form-sub">Start your fitness journey now</div>
          <div class="auth-err" id="reg-err"></div>
          <div class="field"><label class="field-label">Full name</label><input class="field-input" id="r-name" placeholder="Your name"></div>
          <div class="field"><label class="field-label">Email address</label><input class="field-input" id="r-email" type="email" placeholder="you@email.com"></div>
          <div class="field"><label class="field-label">Password (min 6 chars)</label><input class="field-input" id="r-pass" type="password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;"></div>
          <button class="btn-volt" onclick="doRegister()">Create Account &rarr;</button>
        </div>
      </div>
    </div>
  </div>

  '''
    html = html[:auth_start] + new_auth + html[app_start:]
    print('OK: Auth screen HTML replaced')
else:
    print(f'SKIP: auth_start={auth_start}, app_start={app_start}')

# =========================================================
# PART 3: Save
# =========================================================
with open(r'C:\Users\ajaok\OneDrive\Desktop\FitnessApp\frontend\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'File saved, new length: {len(html)}')
