// API integration for Best Buy Listing System
const API_BASE_URL = 'http://localhost:5000/api';

class BestBuyAPI {
  async request(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`;
    const config = {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    };

    try {
      const response = await fetch(url, config);
      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.message || 'API request failed');
      }
      
      return data;
    } catch (error) {
      console.error('API request error:', error);
      throw error;
    }
  }

  // Health check
  async healthCheck() {
    return this.request('/health');
  }

  // Validate listing data
  async validateListing(formData) {
    return this.request('/validate', {
      method: 'POST',
      body: JSON.stringify(formData),
    });
  }

  // Generate template
  async generateTemplate(formData) {
    return this.request('/generate-template', {
      method: 'POST',
      body: JSON.stringify(formData),
    });
  }

  // Get hierarchy codes
  async getHierarchyCodes() {
    return this.request('/hierarchy-codes');
  }

  // Generate SKU
  async generateSKU(productData) {
    return this.request('/generate-sku', {
      method: 'POST',
      body: JSON.stringify(productData),
    });
  }

  // Get field information
  async getFieldInfo() {
    return this.request('/field-info');
  }

  // List templates
  async listTemplates() {
    return this.request('/templates');
  }

  // Download template
  getDownloadUrl(filename) {
    return `${API_BASE_URL}/download-template/${filename}`;
  }
}

export default new BestBuyAPI();

