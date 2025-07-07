# Quick Deployment Steps

## 1. Upload to GitHub
- Create new repository
- Upload all project files
- Don't commit API keys

## 2. Deploy to Vercel
- Connect GitHub repo to Vercel
- Add environment variables:
  - `PAYSTACK_PUBLIC_KEY`
  - `PAYSTACK_SECRET_KEY`
- Deploy automatically

## 3. Update Paystack
- Add your Vercel domain to Paystack allowed domains
- Test payment flow

## 4. Verify
- Test user registration
- Test payment buttons
- Verify plan upgrades work

See `VERCEL_DEPLOYMENT_GUIDE.md` for complete instructions.