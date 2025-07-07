# Paystack Setup Guide for Decision AI

## Overview
This guide provides step-by-step instructions for setting up payment plans on Paystack for your Decision AI application.

## Prerequisites
- Paystack account (sign up at https://paystack.com)
- Nigerian bank account (for payouts)
- Valid business registration (for full account verification)

## Step 1: Create Paystack Account

1. Visit https://paystack.com and click "Get Started"
2. Fill in your business information:
   - Business Name: Decision AI
   - Business Type: Software/Technology
   - Industry: Software as a Service (SaaS)
   - Website: Your app's URL
3. Verify your email address
4. Complete phone verification

## Step 2: Business Verification

1. Log into your Paystack dashboard
2. Navigate to "Settings" → "Business Profile"
3. Upload required documents:
   - Certificate of Incorporation (CAC)
   - Memorandum & Articles of Association
   - Bank account details
   - Valid ID of directors
4. Wait for verification (usually 1-3 business days)

## Step 3: Get API Keys

1. Go to "Settings" → "API Keys & Webhooks"
2. Copy your keys:
   - **Public Key**: Starts with `pk_test_` (for testing) or `pk_live_` (for production)
   - **Secret Key**: Starts with `sk_test_` (for testing) or `sk_live_` (for production)
3. Store these securely - they're already configured in your Replit environment

## Step 4: Create Payment Plans

### Plan 1: Basic Plan (₦3,999/month)
1. Navigate to "Payments" → "Plans" in your dashboard
2. Click "Create Plan"
3. Fill in details:
   - **Plan Name**: Decision AI Basic
   - **Plan Code**: decision-ai-basic
   - **Amount**: ₦3,999 (approximately $9.99)
   - **Interval**: Monthly
   - **Description**: 50 decision analyses, advanced charts, decision history, export reports
4. Click "Create Plan"

### Plan 2: Professional Plan (₦3,999/month)
1. Click "Create Plan" again
2. Fill in details:
   - **Plan Name**: Decision AI Professional
   - **Plan Code**: decision-ai-professional
   - **Amount**: ₦3,999 (approximately $9.99)
   - **Interval**: Monthly
   - **Description**: Unlimited AI analyses, advanced insights, priority processing, PDF export, email support
3. Click "Create Plan"

### Plan 3: Premium Plan (₦9,999/month)
1. Click "Create Plan" again
2. Fill in details:
   - **Plan Name**: Decision AI Premium
   - **Plan Code**: decision-ai-premium
   - **Amount**: ₦9,999 (approximately $24.99)
   - **Interval**: Monthly
   - **Description**: Everything in Professional plus team collaboration, custom AI models, analytics dashboard, API access, priority support
3. Click "Create Plan"

### Plan 4: Enterprise Plan (₦11,999/month)
1. Click "Create Plan" again
2. Fill in details:
   - **Plan Name**: Decision AI Enterprise
   - **Plan Code**: decision-ai-enterprise
   - **Amount**: ₦11,999 (approximately $29.99)
   - **Interval**: Monthly
   - **Description**: Everything in Premium plus team collaboration, custom AI models, advanced analytics, API access, priority support & training
3. Click "Create Plan"

## Step 5: Configure Webhooks (Optional but Recommended)

1. Go to "Settings" → "API Keys & Webhooks"
2. Click "Add Webhook"
3. Set URL: `https://your-app-url.replit.app/api/paystack-webhook`
4. Select events:
   - `subscription.create`
   - `subscription.disable`
   - `charge.success`
   - `invoice.create`
   - `invoice.payment_failed`
5. Click "Create Webhook"

## Step 6: Test Your Integration

### Test Mode
1. Use test API keys (pk_test_ and sk_test_)
2. Use test card numbers:
   - **Successful Payment**: 4084084084084081
   - **Failed Payment**: 4084084084084082
   - **Insufficient Funds**: 4084084084084083

### Test Cards Details
- **Card Number**: 4084084084084081
- **Expiry Date**: Any future date (e.g., 12/25)
- **CVV**: Any 3 digits (e.g., 123)
- **PIN**: 1234

## Step 7: Go Live

1. Complete business verification
2. Request live API keys
3. Update your Replit secrets with live keys:
   - `PAYSTACK_PUBLIC_KEY`: Your live public key
   - `PAYSTACK_SECRET_KEY`: Your live secret key
4. Update plan amounts to live values
5. Test with small amounts first

## Security Best Practices

1. **Never expose secret keys** in frontend code
2. **Verify all payments** on your backend
3. **Use HTTPS** for all payment pages
4. **Implement webhook verification** for security
5. **Log all transactions** for audit purposes

## Currency Conversion

Since your app shows USD prices but Paystack processes in NGN:
- $9.99 ≈ ₦3,999 (at ~400 NGN/USD)
- $24.99 ≈ ₦9,999
- $29.99 ≈ ₦11,999

Update these amounts based on current exchange rates.

## Integration Status

✅ **Completed**:
- Paystack SDK integrated
- Payment buttons configured
- Success/failure handling
- User plan updates
- Toast notifications
- Loading states

✅ **Payment Flow**:
1. User clicks upgrade button
2. System checks login status
3. Paystack popup opens
4. User enters card details
5. Payment processed
6. Success callback updates user plan
7. User redirected to dashboard

## Support

If you encounter issues:
1. Check Paystack documentation: https://paystack.com/docs
2. Contact Paystack support: support@paystack.com
3. Check your webhook logs in dashboard
4. Verify API key permissions

## Next Steps

1. Set up business verification
2. Create payment plans as outlined above
3. Test with test cards
4. Deploy to production with live keys
5. Monitor transactions in dashboard

Your Paystack integration is now complete and ready for testing!