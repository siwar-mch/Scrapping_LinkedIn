import time
import random
from playwright.sync_api import sync_playwright

# --- CONFIGURATION ---
EMAIL = "toutoumch26@gmail.com"
PASSWORD = "toutou123"
MESSAGE_TEXT = "Hello Mr Ala Kharat"


def human_type(element, text):
    """Simule une frappe humaine pour activer les scripts du site."""
    for char in text:
        element.type(char, delay=random.randint(70, 150))


def main():
    with sync_playwright() as p:
        # Lancement avec interface pour observation
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1280, "height": 700})
        page = context.new_page()

        try:
            # --- ÉTAPE 1 : AUTHENTICATION ---
            print("--- ÉTAPE 1 : CONNEXION ---")
            page.goto("https://www.linkedin.com/login")

            # Typing email (human-like)
            email_input = page.get_by_label("Email or Phone")
            email_input.click()
            human_type(email_input, EMAIL)
            time.sleep(1)

            # Typing password (human-like)
            password_input = page.get_by_label("Password")
            password_input.click()
            human_type(password_input, PASSWORD)
            time.sleep(1)

            page.get_by_role("button", name="Sign in", exact=True).click()

            page.wait_for_url("**/feed/**", timeout=60000)
            print("✅ Authentification réussie.")

            # --- ÉTAPE 2 : ACCÈS AUX RELATIONS ---
            print("--- ÉTAPE 2 : ACCÈS AUX RELATIONS ---")
            page.goto(
                "https://www.linkedin.com/mynetwork/invite-connect/connections/",
                wait_until="domcontentloaded",
            )

            print("Attente du bouton Message...")
            msg_btn = page.locator("button:has-text('Message')").first
            msg_btn.wait_for(state="visible", timeout=15000)
            msg_btn.click()
            print("✅ Fenêtre de chat ouverte.")
            time.sleep(3)

            # --- ÉTAPE 3 : ENVOI SÉCURISÉ ---
            print("--- ÉTAPE 3 : ENVOI DU MESSAGE ---")
            chat_box = page.locator("div.msg-form__contenteditable").first
            chat_box.click()

            human_type(chat_box, MESSAGE_TEXT)
            print(f"Message saisi : {MESSAGE_TEXT}")
            time.sleep(2)

            send_btn = page.locator("button.msg-form__send-button").first

            if send_btn.is_visible() and send_btn.is_enabled():
                print("Clic sur le bouton Envoyer...")
                send_btn.click()
            else:
                print("Bouton bloqué, utilisation de la touche Entrée...")
                page.keyboard.press("Enter")

            print("🚀 Action terminée avec succès !")

            # Preuve pour le rapport
            time.sleep(2)
            page.screenshot(path="preuve_succes_m4c1.png")

        except Exception as e:
            print(f"❌ Erreur : {e}")
            page.screenshot(path="erreur_rapport.png")

        finally:
            print("Fin du script. Fermeture dans 5s...")
            time.sleep(5)
            context.close()
            browser.close()


if __name__ == "__main__":
    main()
