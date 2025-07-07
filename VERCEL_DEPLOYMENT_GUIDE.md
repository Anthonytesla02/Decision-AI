# Vercel Deployment Guide for Decision AI

## Overview
This guide will help you deploy your Decision AI application to Vercel with full Paystack payment integration. The app is a static site that will work perfectly on Vercel's platform.

## Prerequisites
- A Vercel account (sign up at https://vercel.com)
- Your Paystack API keys (public and secret)
- GitHub account (recommended for continuous deployment)

## Step 1: Prepare Your Repository

### 1.1 Upload to GitHub
1. Create a new repository on GitHub
2. Upload all your project files to the repository
3. Make sure these files are included:
   - `index.html`
   - `script.js`
   - `styles.css`
   - `config.js`
   - `vercel.json`
   - `PAYSTACK_SETUP_GUIDE.md`
   - `VERCEL_DEPLOYMENT_GUIDE.md`

### 1.2 Important Files for Vercel
- `vercel.json` - Vercel configuration (already created)
- `config.js` - API configuration file
- All HTML, CSS, and JS files

## Step 2: Deploy to Vercel

### 2.1 Connect GitHub Repository
1. Go to https://vercel.com/dashboard
2. Click "New Project"
3. Import your GitHub repository
4. Select your Decision AI repository

### 2.2 Configure Build Settings
Vercel will automatically detect this as a static site. No build configuration needed!

### 2.3 Environment Variables Setup
**IMPORTANT**: You must add these environment variables in the Vercel dashboard:

1. Go to your project in Vercel dashboard
2. Click on **Settings** tab
3. Click on **Environment Variables** in the sidebar
4. Add these variables one by one:

**Variable 1:**
- Name: `PAYSTACK_PUBLIC_KEY`
- Value: `your_paystack_public_key_here` (starts with pk_test_ or pk_live_)
- Environment: Production, Preview, Development (select all)

**Variable 2:**
- Name: `PAYSTACK_SECRET_KEY`
- Value: `your_paystack_secret_key_here` (starts with sk_test_ or sk_live_)
- Environment: Production, Preview, Development (select all)

**After adding variables:**
- Click **Save** for each variable
- **Redeploy** your application (go to Deployments tab and click "Redeploy")

**Important**: 
- Use your **LIVE** Paystack keys for production
- Use your **TEST** keys for testing
- Never commit these keys to your repository

### 2.4 Deploy
1. Click "Deploy"
2. Wait for deployment to complete
3. You'll get a live URL like: `https://your-app-name.vercel.app`

## Step 3: Configure Paystack for Your Domain

### 3.1 Update Paystack Settings
1. Log into your Paystack dashboard
2. Go to Settings → API Keys & Webhooks
3. Add your Vercel domain to allowed domains:
   - `https://your-app-name.vercel.app`
   - `https://your-custom-domain.com` (if using custom domain)

### 3.2 Test Payment Integration
1. Visit your deployed app
2. Register a new account
3. Try upgrading to a paid plan
4. Use Paystack test cards to verify payment flow

## Step 4: Custom Domain (Optional)

### 4.1 Add Custom Domain
1. In Vercel dashboard, go to Settings → Domains
2. Add your custom domain (e.g., `decisai.com`)
3. Configure DNS settings as shown by Vercel
4. SSL certificate will be automatically provisioned

### 4.2 Update Paystack Settings
Add your custom domain to Paystack allowed domains list.

## Step 5: Verify Everything Works

### 5.1 Test Core Features
- [ ] App loads correctly
- [ ] User registration works
- [ ] Login/logout functions
- [ ] Decision analysis works
- [ ] Payment buttons appear
- [ ] Paystack popup opens

### 5.2 Test Payment Flow
- [ ] Click upgrade button
- [ ] Paystack payment modal opens
- [ ] Test payment completes
- [ ] User plan updates correctly
- [ ] Credits are allocated

## Troubleshooting

### Common Issues & Solutions

#### 1. "Payment system not configured" Error
**Solution**: Verify environment variables are set in Vercel dashboard
```
Settings → Environment Variables
PAYSTACK_PUBLIC_KEY = pk_test_... or pk_live_...
PAYSTACK_SECRET_KEY = sk_test_... or sk_live_...
```

#### 2. Paystack Popup Not Opening
**Solution**: Check browser console for errors. Ensure:
- Paystack script is loading
- API keys are valid
- Domain is whitelisted in Paystack

#### 3. Payment Completes But Plan Doesn't Update
**Solution**: 
- Check if plan codes match your Paystack setup
- Verify amounts are correct (in pesewas, not cedis)
- Current plan codes:
  - Basic: `PLN_nzh240uvvavt1wr` (2 cedis = 200 pesewas)
  - Professional: `PLN_sh1x79iqqxvj20m` (100 cedis = 10,000 pesewas)
  - Premium: `PLN_e3cd7974vply6c1` (250 cedis = 25,000 pesewas)

#### 4. CSS/JavaScript Not Loading (App Looks Raw)
**Problem**: Static assets (CSS/JS) aren't loading, app appears unstyled
**Solution**: 
- Ensure your `vercel.json` is simplified (should only contain `{"version": 2}`)
- Check that all files are in the root directory of your repository
- Verify file paths in `index.html` are correct (should be `href="styles.css"`, `src="script.js"`)
- Redeploy after making changes

#### 5. CORS Errors
**Solution**: Add your Vercel domain to Paystack allowed domains

## Deployment Checklist

### Before Deployment
- [ ] All files uploaded to GitHub
- [ ] Environment variables prepared
- [ ] Paystack plan codes verified
- [ ] Test API keys working locally

### During Deployment
- [ ] Repository connected to Vercel
- [ ] Environment variables configured
- [ ] Build successful
- [ ] Domain configured (if using custom)

### After Deployment
- [ ] App loads without errors
- [ ] User registration works
- [ ] Payment flow tested
- [ ] Paystack domain whitelist updated
- [ ] All features verified

## Pricing Structure (Ghana Cedis)

Your current pricing:
- **Basic Plan**: 2 GHS (200 pesewas)
- **Professional Plan**: 100 GHS (10,000 pesewas)
- **Premium Plan**: 250 GHS (25,000 pesewas)

## Support

### If You Need Help
1. Check Vercel deployment logs
2. Check browser console for JavaScript errors
3. Verify Paystack dashboard for payment issues
4. Test with Paystack test cards first

### Paystack Test Cards
- **Successful Payment**: 4084084084084081
- **Declined Payment**: 4084084084084081 (with CVV 408)

## Advanced Configuration

### Custom Domain with SSL
Vercel automatically provides SSL certificates for custom domains. Just add your domain in the Vercel dashboard.

### Continuous Deployment
Once connected to GitHub, any push to your main branch will automatically deploy to Vercel.

### Environment-Specific Configuration
- Use test API keys for development
- Use live API keys for production
- You can create separate Vercel projects for staging and production

## Security Notes

- Never commit API keys to your repository
- Use environment variables for all sensitive data
- Regularly rotate your Paystack secret keys
- Monitor payment transactions in Paystack dashboard

## Maintenance

### Regular Tasks
- Monitor application performance in Vercel dashboard
- Check payment success rates in Paystack
- Update API keys when needed
- Review error logs regularly

Your Decision AI app is now ready for production deployment on Vercel!