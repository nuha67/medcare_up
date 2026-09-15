from database import SessionLocal
from models import User
from passlib.context import CryptContext

# Bcrypt Hashing Setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_super_admin():
    db = SessionLocal()
    
    # දැනටමත් Admin කෙනෙක් ඉන්නවද කියලා බැලීම
    existing_admin = db.query(User).filter(User.username == "superadmin").first()
    
    if existing_admin:
        print("⚠️ Admin account already exists!")
    else:
        # අලුත් Admin ගේ Password එක (උදා: Admin@1234) Hash කිරීම
        hashed_pw = pwd_context.hash("Admin@1234")
        
        new_admin = User(
            username="superadmin",
            email="admin@medcare.com",
            hashed_password=hashed_pw,
            role="Admin",
            is_active=True
        )
        
        db.add(new_admin)
        db.commit()
        print("✅ Super Admin created successfully! You can now login.")
        print("👉 Username: superadmin")
        print("👉 Password: Admin@1234")

    db.close()

if __name__ == "__main__":
    create_super_admin()
