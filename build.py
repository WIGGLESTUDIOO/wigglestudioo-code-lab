# Run: python3 build.py   -> rewrites data.js from the groups below + files in demos/ and downloads/
import json
YT = "https://youtube.com/@WiggleStudioo"
S = lambda i: "https://youtube.com/shorts/" + i if i else ""
# ---- ADD NEW CARDS / SECTIONS HERE ----
GROUPS = [
 dict(title="Little components", emoji="🍬", desc="Small things from my Shorts. Paste them into any project.", video="", short="", zip="", items=[
  dict(id="login", emoji="🌸", title="Animated Login Form", desc="Floating labels and a show/hide password button.", tags=["HTML","CSS"], video=S("CYlmh0Jl6sY")),
  dict(id="otp", emoji="🍓", title="OTP Input Boxes", desc="Auto-jumping boxes that check the code. Try 1234!", tags=["HTML","CSS","JS"], video=S("RfwfxwMYtv4")),
  dict(id="navbar", emoji="🫧", title="Sticky Glass Navbar", desc="Glass blur, underline hover, shrinks on scroll.", tags=["HTML","CSS","JS"], video=S("vCM7XuOBDpc")),
  dict(id="toggle", emoji="🌙", title="Dark / Light Toggle", desc="A smooth switch that changes the whole mood.", tags=["HTML","CSS","JS"], video=S("4Xy79_qWkIw")),
  dict(id="floating_cards", emoji="☁️", title="Floating Cards", desc="One hover rule lifts the cards up with a soft glow.", tags=["HTML","CSS"], video=S("JR6FBuWOG6Y")),
  dict(id="typing", emoji="✨", title="Typing Effect", desc="Text that types and deletes itself.", tags=["HTML","JS"], video=""),
  dict(id="progress", emoji="🍡", title="Scroll Progress Bar", desc="A bar that grows as you scroll.", tags=["HTML","CSS","JS"], video=""),
  dict(id="accordion", emoji="🍰", title="FAQ Accordion", desc="Answers that slide open smoothly.", tags=["HTML","CSS","JS"], video=""),
  dict(id="copy", emoji="💌", title="Copy Button", desc="Copy to clipboard with a Copied! message.", tags=["HTML","JS"], video=""),
 ]),
 dict(title="Portfolio Website", emoji="🎀", desc="Long video: build a full portfolio from an empty folder. Navbar, typing hero, projects grid, dark mode, contact form.", video="", short="", zip="downloads/portfolio_website_code.zip", items=[
  dict(title="Portfolio Website", emoji="🎀", desc="3 files: index.html, style.css, script.js.", tags=["HTML","CSS","JS"], img="img/portfolio.jpg", zip="downloads/portfolio_website_code.zip", video=""),
 ]),
 dict(title="Login & Sign Up Page", emoji="🧸", desc="Long video: glass card, floating labels, validation, sign up mode and a strength bar.", video="", short=S("CYlmh0Jl6sY"), zip="downloads/login_signup_code.zip", items=[
  dict(title="Login & Sign Up Page", emoji="🧸", desc="3 files: index.html, style.css, script.js.", tags=["HTML","CSS","JS"], img="img/login.jpg", zip="downloads/login_signup_code.zip", video=""),
 ]),
 dict(title="10 Adorable CSS Buttons", emoji="💗", desc="Long video: 10 satisfying buttons with HTML and CSS. Each page has two buttons.", video="", short=S("DoebFQD4pTw"), zip="downloads/css_buttons_code.zip", items=[
  dict(id="btn_press_shine", emoji="🍬", title="Press & Shine", desc="Squishy press button and a shine sweep.", tags=["HTML","CSS"], video=""),
  dict(id="btn_slide_arrow", emoji="💌", title="Slide & Arrow", desc="A slide fill button and an arrow that moves.", tags=["HTML","CSS"], video=""),
  dict(id="btn_jelly_glow", emoji="🫧", title="Jelly & Glow", desc="A wobbly jelly button and a glowing one.", tags=["HTML","CSS"], video=""),
  dict(id="btn_ripple_heart", emoji="💓", title="Ripple & Heart", desc="A ripple click effect and a heart like button.", tags=["HTML","CSS","JS"], video=""),
  dict(id="btn_switch_load", emoji="🌷", title="Switch & Loading", desc="A toggle switch and a loading button.", tags=["HTML","CSS","JS"], video=""),
 ]),
 dict(title="5 Useful Tools", emoji="🧰", desc="Long video: five useful tools with HTML, CSS and JavaScript.", video="", short="", zip="downloads/cute_useful_tools_code.zip", items=[
  dict(id="tool_timer", emoji="⏰", title="Study Timer", desc="A round timer with start and reset.", tags=["HTML","CSS","JS"], video=""),
  dict(id="tool_password", emoji="🔐", title="Password Maker", desc="Pick a length and make a strong password.", tags=["HTML","CSS","JS"], video=""),
  dict(id="tool_palette", emoji="🎨", title="Palette Maker", desc="Make color palettes and tap a color to copy it.", tags=["HTML","CSS","JS"], video=""),
  dict(id="tool_countdown", emoji="🎂", title="Countdown", desc="Days, hours, minutes and seconds to a date. Change the date in the code!", tags=["HTML","CSS","JS"], video=""),
  dict(id="tool_todo", emoji="📝", title="To-Do List", desc="Add, tick and delete tasks.", tags=["HTML","CSS","JS"], video=""),
 ]),
 dict(title="5 Cute Gift Cards", emoji="🎁", desc="Long video: five digital gift cards made with code.", video="", short="", zip="downloads/cute_cards_code.zip", items=[
  dict(id="card_flip", emoji="🧸", title="Flip Card", desc="A card that flips over to show a message.", tags=["HTML","CSS","JS"], video=S("2gPvguimdAA")),
  dict(id="card_envelope", emoji="💌", title="Love Letter Envelope", desc="Open the envelope to read the letter.", tags=["HTML","CSS","JS"], video=S("V5Ve5QcORoM")),
  dict(id="card_popup_heart", emoji="💗", title="Pop-up Heart", desc="Tap the heart and it pops with a surprise.", tags=["HTML","CSS","JS"], video=S("adEFnUXW7NI")),
  dict(id="card_scratch", emoji="🎟️", title="Scratch Card", desc="Scratch with your finger to reveal a message.", tags=["HTML","CSS","JS"], video=""),
  dict(id="card_birthday", emoji="🎂", title="Birthday Card", desc="Blow out the candle and make a wish. Change the name in the code!", tags=["HTML","CSS","JS"], video=S("F4_pMBwtmSM")),
 ]),
 dict(title="5 Cute Mini Games", emoji="🎮", desc="Long video: five little games with HTML, CSS and JavaScript. Play them right here!", video="", short="", zip="downloads/cute_mini_games_code.zip", items=[
  dict(id="game_ttt", emoji="⭕", title="Tic Tac Toe", desc="Play against a friend. Hearts and stars instead of X and O.", tags=["HTML","CSS","JS"], video=""),
  dict(id="game_memory", emoji="🃏", title="Memory Match", desc="Flip the cards and find the pairs.", tags=["HTML","CSS","JS"], video=""),
  dict(id="game_mole", emoji="🔨", title="Whack-a-Mole", desc="Tap the moles before they hide.", tags=["HTML","CSS","JS"], video=""),
  dict(id="game_guess", emoji="🔢", title="Guess the Number", desc="Higher or lower? Find the secret number.", tags=["HTML","CSS","JS"], video=""),
  dict(id="game_snake", emoji="🐍", title="Snake", desc="Eat the apples and do not hit the wall. Use arrow keys.", tags=["HTML","CSS","JS"], video=""),
 ]),
 dict(title="Cute Bakery Website", emoji="🧁", desc="Long video: build a whole bakery website from an empty folder, with a working cart counter.", video="", short="", zip="downloads/bakery_website_code.zip", items=[
  dict(title="Cute Bakery Website", emoji="🧁", desc="3 files plus pictures: index.html, style.css, script.js, img folder.", tags=["HTML","CSS","JS"], img="img/bakery.jpg", zip="downloads/bakery_website_code.zip", video=""),
 ]),
 dict(title="Love Letter That Types Itself", emoji="💌", desc="Long video: an envelope made with CSS opens and the letter types itself. Add ?to=YourName to the link!", video="", short="", zip="downloads/love_letter_code.zip", items=[
  dict(id="loveletter", emoji="💌", title="Love Letter", desc="Press Open. The envelope opens, the message types, hearts fall.", tags=["HTML","CSS","JS"], video=""),
 ]),
 dict(title="Python Art", emoji="🐍", desc="Long video: can you guess what this code draws? Run it yourself and see all the pictures.", video="", short="", zip="", items=[
  dict(id="guess_the_code", file="downloads/guess_the_code.py", emoji="🐍", title="Can You Guess What This Code Draws?", desc="11 drawings in one file: circle, spiral, flower, stars, waves, mandala, tree, snowflake, galaxy, lightning, aurora. Needs: pip install pillow numpy", tags=["Python"], img="img/guess_the_code.jpg", dl="downloads/guess_the_code.py", video=""),
 ]),
]
for g in GROUPS:
    for it in g["items"]:
        if it.get("premium") or "id" not in it: continue
        path = it.get("file") or f"demos/{it['id']}.html"
        it["code"] = open(path, encoding="utf-8").read()
        it["dl"] = it.get("dl") or path
open("data.js", "w").write("const SITE=" + json.dumps(dict(yt=YT, groups=GROUPS), ensure_ascii=False) + ";\n")
print(sum(len(g["items"]) for g in GROUPS), "cards in", len(GROUPS), "sections")
