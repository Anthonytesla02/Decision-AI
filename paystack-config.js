// Simple configuration file for Paystack integration
// This will be loaded by the main application

// Get Paystack keys from environment variables
const PAYSTACK_PUBLIC_KEY = process.env.PAYSTACK_PUBLIC_KEY;
const PAYSTACK_SECRET_KEY = process.env.PAYSTACK_SECRET_KEY;

// Update the APP_CONFIG with actual keys
if (typeof window !== 'undefined' && window.APP_CONFIG) {
    window.APP_CONFIG.PAYSTACK_PUBLIC_KEY = PAYSTACK_PUBLIC_KEY;
    window.APP_CONFIG.PAYSTACK_SECRET_KEY = PAYSTACK_SECRET_KEY;
}

// Export for Node.js environment
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        PAYSTACK_PUBLIC_KEY,
        PAYSTACK_SECRET_KEY
    };
}