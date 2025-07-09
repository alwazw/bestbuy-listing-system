import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Label } from '@/components/ui/label.jsx'
import { Textarea } from '@/components/ui/textarea.jsx'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { Progress } from '@/components/ui/progress.jsx'
import { Alert, AlertDescription } from '@/components/ui/alert.jsx'
import { AlertCircle, CheckCircle2, Package, FileText, Image, Settings, Download, Upload, Loader2 } from 'lucide-react'
import BestBuyAPI from './api.js'
import './App.css'

function App() {
  const [formData, setFormData] = useState({
    // Core Product Information
    shop_sku: '',
    title: '',
    short_description: '',
    long_description: '',
    brand_name: '',
    model_number: '',
    mpn: '',
    product_condition: '',
    category_code: '',
    web_hierarchy: '',
    
    // Technical Specifications
    processor_brand: '',
    processor_model: '',
    memory_size: '',
    storage_capacity: '',
    storage_type: '',
    screen_size: '',
    screen_resolution: '',
    operating_system: '',
    
    // Pricing and Inventory
    price: '',
    msrp: '',
    quantity: '',
    
    // Images
    images: [],
    
    // Variant Information
    variant_group: '',
    platform: '',
    
    // Physical Specifications
    weight: '',
    dimensions: '',
    color: ''
  })

  const [currentTab, setCurrentTab] = useState('basic')
  const [validationErrors, setValidationErrors] = useState({})
  const [completionProgress, setCompletionProgress] = useState(0)
  const [isLoading, setIsLoading] = useState(false)
  const [apiStatus, setApiStatus] = useState('checking')
  const [hierarchyCodes, setHierarchyCodes] = useState([])
  const [generatedTemplate, setGeneratedTemplate] = useState(null)
  const [alerts, setAlerts] = useState([])

  const conditionOptions = [
    'Brand New',
    'Open Box', 
    'Refurbished (Excellent)',
    'Refurbished (Good)',
    'Refurbished (Fair)'
  ]

  const platformOptions = [
    'PC Laptop',
    'Gaming',
    'MacBook'
  ]

  // Initialize API connection and load data
  useEffect(() => {
    initializeApp()
  }, [])

  const initializeApp = async () => {
    try {
      // Check API health
      await BestBuyAPI.healthCheck()
      setApiStatus('connected')
      
      // Load hierarchy codes
      const hierarchyResponse = await BestBuyAPI.getHierarchyCodes()
      if (hierarchyResponse.success) {
        setHierarchyCodes(hierarchyResponse.codes)
      }
      
    } catch (error) {
      console.error('Failed to initialize app:', error)
      setApiStatus('error')
      addAlert('error', 'Failed to connect to backend API')
    }
  }

  const addAlert = (type, message) => {
    const alert = {
      id: Date.now(),
      type,
      message
    }
    setAlerts(prev => [...prev, alert])
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
      setAlerts(prev => prev.filter(a => a.id !== alert.id))
    }, 5000)
  }

  const handleInputChange = (field, value) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }))
    
    // Clear validation error when user starts typing
    if (validationErrors[field]) {
      setValidationErrors(prev => ({
        ...prev,
        [field]: null
      }))
    }
    
    // Update completion progress
    updateCompletionProgress()
  }

  const updateCompletionProgress = () => {
    const requiredFields = [
      'shop_sku', 'title', 'short_description', 'long_description',
      'brand_name', 'model_number', 'mpn', 'product_condition',
      'category_code', 'web_hierarchy'
    ]
    
    const completedFields = requiredFields.filter(field => formData[field]?.toString().trim())
    const progress = (completedFields.length / requiredFields.length) * 100
    setCompletionProgress(progress)
  }

  const generateSKU = async () => {
    if (!formData.brand_name || !formData.model_number) {
      addAlert('error', 'Brand name and model number are required for SKU generation')
      return
    }

    setIsLoading(true)
    try {
      const response = await BestBuyAPI.generateSKU({
        brand_name: formData.brand_name,
        model_number: formData.model_number,
        memory_size: formData.memory_size,
        storage_capacity: formData.storage_capacity
      })
      
      if (response.success) {
        handleInputChange('shop_sku', response.sku)
        addAlert('success', `SKU generated: ${response.sku}`)
      }
    } catch (error) {
      addAlert('error', `Failed to generate SKU: ${error.message}`)
    } finally {
      setIsLoading(false)
    }
  }

  const validateForm = async () => {
    setIsLoading(true)
    try {
      const response = await BestBuyAPI.validateListing(formData)
      
      if (response.success) {
        const validation = response.validation
        setValidationErrors(validation.errors || {})
        
        if (validation.is_valid) {
          addAlert('success', 'All validation checks passed!')
        } else {
          addAlert('error', 'Validation errors found. Please check the form.')
        }
        
        if (validation.warnings && validation.warnings.length > 0) {
          validation.warnings.forEach(warning => {
            addAlert('warning', warning)
          })
        }
      }
    } catch (error) {
      addAlert('error', `Validation failed: ${error.message}`)
    } finally {
      setIsLoading(false)
    }
  }

  const exportTemplate = async () => {
    setIsLoading(true)
    try {
      const response = await BestBuyAPI.generateTemplate(formData)
      
      if (response.success) {
        setGeneratedTemplate(response)
        addAlert('success', 'Template generated successfully!')
        
        // Auto-download the file
        const filename = response.file_path.split('/').pop()
        const downloadUrl = BestBuyAPI.getDownloadUrl(filename)
        
        const link = document.createElement('a')
        link.href = downloadUrl
        link.download = filename
        document.body.appendChild(link)
        link.click()
        document.body.removeChild(link)
        
      } else {
        setValidationErrors(response.errors || {})
        addAlert('error', response.message || 'Template generation failed')
      }
    } catch (error) {
      addAlert('error', `Template generation failed: ${error.message}`)
    } finally {
      setIsLoading(false)
    }
  }

  const importData = () => {
    // This would allow importing existing product data
    addAlert('info', 'Import functionality will be implemented in v2')
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="max-w-6xl mx-auto">
        {/* Alerts */}
        <div className="fixed top-4 right-4 z-50 space-y-2">
          {alerts.map(alert => (
            <Alert key={alert.id} className={`w-80 ${
              alert.type === 'error' ? 'border-red-500 bg-red-50' :
              alert.type === 'success' ? 'border-green-500 bg-green-50' :
              alert.type === 'warning' ? 'border-yellow-500 bg-yellow-50' :
              'border-blue-500 bg-blue-50'
            }`}>
              <AlertCircle className="h-4 w-4" />
              <AlertDescription>{alert.message}</AlertDescription>
            </Alert>
          ))}
        </div>

        {/* Header */}
        <div className="mb-8">
          <div className="flex items-center justify-between mb-4">
            <div>
              <h1 className="text-4xl font-bold text-gray-900 mb-2">Best Buy Listing Creator</h1>
              <p className="text-lg text-gray-600">Streamlined marketplace listing management with automated template generation</p>
            </div>
            <div className="flex items-center gap-2">
              <div className={`w-3 h-3 rounded-full ${
                apiStatus === 'connected' ? 'bg-green-500' :
                apiStatus === 'error' ? 'bg-red-500' :
                'bg-yellow-500'
              }`}></div>
              <span className="text-sm text-gray-600">
                API {apiStatus === 'connected' ? 'Connected' : apiStatus === 'error' ? 'Error' : 'Checking...'}
              </span>
            </div>
          </div>
          
          {/* Progress Bar */}
          <div className="mt-4">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm font-medium text-gray-700">Completion Progress</span>
              <span className="text-sm text-gray-500">{Math.round(completionProgress)}%</span>
            </div>
            <Progress value={completionProgress} className="h-2" />
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex gap-4 mb-6">
          <Button onClick={importData} variant="outline" className="flex items-center gap-2">
            <Upload className="h-4 w-4" />
            Import Data
          </Button>
          <Button onClick={validateForm} variant="outline" className="flex items-center gap-2" disabled={isLoading}>
            {isLoading ? <Loader2 className="h-4 w-4 animate-spin" /> : <CheckCircle2 className="h-4 w-4" />}
            Validate
          </Button>
          <Button onClick={exportTemplate} className="flex items-center gap-2" disabled={isLoading}>
            {isLoading ? <Loader2 className="h-4 w-4 animate-spin" /> : <Download className="h-4 w-4" />}
            Export Template
          </Button>
          <Button onClick={generateSKU} variant="secondary" className="flex items-center gap-2" disabled={isLoading}>
            {isLoading ? <Loader2 className="h-4 w-4 animate-spin" /> : <Settings className="h-4 w-4" />}
            Generate SKU
          </Button>
        </div>

        {/* Generated Template Info */}
        {generatedTemplate && (
          <Card className="mb-6 border-green-200 bg-green-50">
            <CardHeader>
              <CardTitle className="text-green-800">Template Generated Successfully</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-2 md:grid-cols-3 gap-4 text-sm">
                <div>
                  <span className="font-medium">SKU:</span> {generatedTemplate.summary.sku}
                </div>
                <div>
                  <span className="font-medium">Brand:</span> {generatedTemplate.summary.brand}
                </div>
                <div>
                  <span className="font-medium">Category:</span> {generatedTemplate.summary.category}
                </div>
                <div>
                  <span className="font-medium">Condition:</span> {generatedTemplate.summary.condition}
                </div>
                <div>
                  <span className="font-medium">Fields:</span> {generatedTemplate.summary.fields_populated}
                </div>
              </div>
            </CardContent>
          </Card>
        )}

        {/* Main Form */}
        <Tabs value={currentTab} onValueChange={setCurrentTab} className="space-y-6">
          <TabsList className="grid w-full grid-cols-5">
            <TabsTrigger value="basic" className="flex items-center gap-2">
              <Package className="h-4 w-4" />
              Basic Info
            </TabsTrigger>
            <TabsTrigger value="specs" className="flex items-center gap-2">
              <Settings className="h-4 w-4" />
              Specifications
            </TabsTrigger>
            <TabsTrigger value="content" className="flex items-center gap-2">
              <FileText className="h-4 w-4" />
              Content
            </TabsTrigger>
            <TabsTrigger value="media" className="flex items-center gap-2">
              <Image className="h-4 w-4" />
              Media
            </TabsTrigger>
            <TabsTrigger value="advanced" className="flex items-center gap-2">
              <AlertCircle className="h-4 w-4" />
              Advanced
            </TabsTrigger>
          </TabsList>

          {/* Basic Information Tab */}
          <TabsContent value="basic" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Package className="h-5 w-5" />
                  Core Product Information
                </CardTitle>
                <CardDescription>
                  Essential product identification and categorization details
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="space-y-2">
                    <Label htmlFor="shop_sku" className="flex items-center gap-2">
                      Shop SKU <Badge variant="destructive">Required</Badge>
                    </Label>
                    <Input
                      id="shop_sku"
                      value={formData.shop_sku}
                      onChange={(e) => handleInputChange('shop_sku', e.target.value)}
                      placeholder="AS-I7-16-512"
                      maxLength={30}
                      className={validationErrors.shop_sku ? 'border-red-500' : ''}
                    />
                    {validationErrors.shop_sku && (
                      <p className="text-sm text-red-500">{validationErrors.shop_sku}</p>
                    )}
                    <p className="text-xs text-gray-500">Format: Brand-Model-Attribute-RAM-Storage</p>
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="brand_name" className="flex items-center gap-2">
                      Brand Name <Badge variant="destructive">Required</Badge>
                    </Label>
                    <Input
                      id="brand_name"
                      value={formData.brand_name}
                      onChange={(e) => handleInputChange('brand_name', e.target.value)}
                      placeholder="ASUS"
                      maxLength={20}
                      className={validationErrors.brand_name ? 'border-red-500' : ''}
                    />
                    {validationErrors.brand_name && (
                      <p className="text-sm text-red-500">{validationErrors.brand_name}</p>
                    )}
                    <p className="text-xs text-gray-500">Brand only, not store name (max 20 chars)</p>
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="model_number" className="flex items-center gap-2">
                      Model Number <Badge variant="destructive">Required</Badge>
                    </Label>
                    <Input
                      id="model_number"
                      value={formData.model_number}
                      onChange={(e) => handleInputChange('model_number', e.target.value)}
                      placeholder="Vivobook"
                      maxLength={20}
                      className={validationErrors.model_number ? 'border-red-500' : ''}
                    />
                    {validationErrors.model_number && (
                      <p className="text-sm text-red-500">{validationErrors.model_number}</p>
                    )}
                    <p className="text-xs text-gray-500">Simplified model designation</p>
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="mpn" className="flex items-center gap-2">
                      Manufacturer Part Number <Badge variant="destructive">Required</Badge>
                    </Label>
                    <Input
                      id="mpn"
                      value={formData.mpn}
                      onChange={(e) => handleInputChange('mpn', e.target.value)}
                      placeholder="Vivobook"
                      maxLength={30}
                      className={validationErrors.mpn ? 'border-red-500' : ''}
                    />
                    {validationErrors.mpn && (
                      <p className="text-sm text-red-500">{validationErrors.mpn}</p>
                    )}
                    <p className="text-xs text-gray-500">Use model number if no MPN exists</p>
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="product_condition" className="flex items-center gap-2">
                      Product Condition <Badge variant="destructive">Required</Badge>
                    </Label>
                    <Select value={formData.product_condition} onValueChange={(value) => handleInputChange('product_condition', value)}>
                      <SelectTrigger className={validationErrors.product_condition ? 'border-red-500' : ''}>
                        <SelectValue placeholder="Select condition" />
                      </SelectTrigger>
                      <SelectContent>
                        {conditionOptions.map(condition => (
                          <SelectItem key={condition} value={condition}>{condition}</SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                    {validationErrors.product_condition && (
                      <p className="text-sm text-red-500">{validationErrors.product_condition}</p>
                    )}
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="category_code" className="flex items-center gap-2">
                      Category Code <Badge variant="destructive">Required</Badge>
                    </Label>
                    <Select value={formData.category_code} onValueChange={(value) => handleInputChange('category_code', value)}>
                      <SelectTrigger className={validationErrors.category_code ? 'border-red-500' : ''}>
                        <SelectValue placeholder="Select category" />
                      </SelectTrigger>
                      <SelectContent>
                        {hierarchyCodes.map(category => (
                          <SelectItem key={category.value} value={category.value}>
                            {category.label}
                          </SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                    {validationErrors.category_code && (
                      <p className="text-sm text-red-500">{validationErrors.category_code}</p>
                    )}
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="platform" className="flex items-center gap-2">
                      Platform <Badge variant="secondary">Recommended</Badge>
                    </Label>
                    <Select value={formData.platform} onValueChange={(value) => handleInputChange('platform', value)}>
                      <SelectTrigger>
                        <SelectValue placeholder="Select platform" />
                      </SelectTrigger>
                      <SelectContent>
                        {platformOptions.map(platform => (
                          <SelectItem key={platform} value={platform}>{platform}</SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="variant_group" className="flex items-center gap-2">
                      Variant Group <Badge variant="secondary">Recommended</Badge>
                    </Label>
                    <Input
                      id="variant_group"
                      value={formData.variant_group}
                      onChange={(e) => handleInputChange('variant_group', e.target.value)}
                      placeholder="as-i7-win"
                    />
                    <p className="text-xs text-gray-500">Groups related product variants</p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Technical Specifications Tab */}
          <TabsContent value="specs" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Settings className="h-5 w-5" />
                  Technical Specifications
                </CardTitle>
                <CardDescription>
                  Detailed technical attributes and performance specifications
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                  <div className="space-y-2">
                    <Label htmlFor="processor_brand">Processor Brand</Label>
                    <Select value={formData.processor_brand} onValueChange={(value) => handleInputChange('processor_brand', value)}>
                      <SelectTrigger>
                        <SelectValue placeholder="Select processor" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="Intel">Intel</SelectItem>
                        <SelectItem value="AMD">AMD</SelectItem>
                        <SelectItem value="Apple">Apple</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="processor_model">Processor Model</Label>
                    <Input
                      id="processor_model"
                      value={formData.processor_model}
                      onChange={(e) => handleInputChange('processor_model', e.target.value)}
                      placeholder="Core i7-12700H"
                    />
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="memory_size">Memory Size (GB)</Label>
                    <Select value={formData.memory_size} onValueChange={(value) => handleInputChange('memory_size', value)}>
                      <SelectTrigger>
                        <SelectValue placeholder="Select RAM" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="8">8 GB</SelectItem>
                        <SelectItem value="16">16 GB</SelectItem>
                        <SelectItem value="24">24 GB</SelectItem>
                        <SelectItem value="32">32 GB</SelectItem>
                        <SelectItem value="40">40 GB</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="storage_capacity">Storage Capacity (GB)</Label>
                    <Select value={formData.storage_capacity} onValueChange={(value) => handleInputChange('storage_capacity', value)}>
                      <SelectTrigger>
                        <SelectValue placeholder="Select storage" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="256">256 GB</SelectItem>
                        <SelectItem value="512">512 GB</SelectItem>
                        <SelectItem value="1000">1 TB</SelectItem>
                        <SelectItem value="2000">2 TB</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="storage_type">Storage Type</Label>
                    <Select value={formData.storage_type} onValueChange={(value) => handleInputChange('storage_type', value)}>
                      <SelectTrigger>
                        <SelectValue placeholder="Select type" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="SSD">SSD</SelectItem>
                        <SelectItem value="HDD">HDD</SelectItem>
                        <SelectItem value="Hybrid">Hybrid</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="screen_size">Screen Size (inches)</Label>
                    <Input
                      id="screen_size"
                      value={formData.screen_size}
                      onChange={(e) => handleInputChange('screen_size', e.target.value)}
                      placeholder="15.6"
                      type="number"
                      step="0.1"
                    />
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="screen_resolution">Screen Resolution</Label>
                    <Select value={formData.screen_resolution} onValueChange={(value) => handleInputChange('screen_resolution', value)}>
                      <SelectTrigger>
                        <SelectValue placeholder="Select resolution" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="1366 x 768">1366 x 768 (HD)</SelectItem>
                        <SelectItem value="1920 x 1080">1920 x 1080 (Full HD)</SelectItem>
                        <SelectItem value="2560 x 1440">2560 x 1440 (QHD)</SelectItem>
                        <SelectItem value="3840 x 2160">3840 x 2160 (4K)</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="operating_system">Operating System</Label>
                    <Select value={formData.operating_system} onValueChange={(value) => handleInputChange('operating_system', value)}>
                      <SelectTrigger>
                        <SelectValue placeholder="Select OS" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="Windows 11">Windows 11</SelectItem>
                        <SelectItem value="Windows 10">Windows 10</SelectItem>
                        <SelectItem value="macOS">macOS</SelectItem>
                        <SelectItem value="Chrome OS">Chrome OS</SelectItem>
                        <SelectItem value="Linux">Linux</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="color">Color</Label>
                    <Select value={formData.color} onValueChange={(value) => handleInputChange('color', value)}>
                      <SelectTrigger>
                        <SelectValue placeholder="Select color" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="Black">Black</SelectItem>
                        <SelectItem value="Silver">Silver</SelectItem>
                        <SelectItem value="Grey">Grey</SelectItem>
                        <SelectItem value="White">White</SelectItem>
                        <SelectItem value="Blue">Blue</SelectItem>
                        <SelectItem value="Gold">Gold</SelectItem>
                        <SelectItem value="Rose Gold">Rose Gold</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Content Tab */}
          <TabsContent value="content" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <FileText className="h-5 w-5" />
                  Product Content
                </CardTitle>
                <CardDescription>
                  Titles, descriptions, and marketing content for your listing
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="space-y-2">
                  <Label htmlFor="title" className="flex items-center gap-2">
                    Product Title <Badge variant="destructive">Required</Badge>
                  </Label>
                  <Input
                    id="title"
                    value={formData.title}
                    onChange={(e) => handleInputChange('title', e.target.value)}
                    placeholder="ASUS Vivobook Laptop - Refurbished Excellent"
                    maxLength={180}
                    className={validationErrors.title ? 'border-red-500' : ''}
                  />
                  {validationErrors.title && (
                    <p className="text-sm text-red-500">{validationErrors.title}</p>
                  )}
                  <div className="flex justify-between text-xs text-gray-500">
                    <span>Must end with condition (e.g., "- Refurbished Excellent")</span>
                    <span>{formData.title.length}/180</span>
                  </div>
                </div>

                <div className="space-y-2">
                  <Label htmlFor="short_description" className="flex items-center gap-2">
                    Short Description <Badge variant="destructive">Required</Badge>
                  </Label>
                  <Textarea
                    id="short_description"
                    value={formData.short_description}
                    onChange={(e) => handleInputChange('short_description', e.target.value)}
                    placeholder="High-performance laptop with Intel i7 processor, perfect for business and productivity tasks."
                    maxLength={480}
                    rows={3}
                    className={validationErrors.short_description ? 'border-red-500' : ''}
                  />
                  {validationErrors.short_description && (
                    <p className="text-sm text-red-500">{validationErrors.short_description}</p>
                  )}
                  <div className="flex justify-between text-xs text-gray-500">
                    <span>No external references, retailer names, or HTML allowed</span>
                    <span>{formData.short_description.length}/480</span>
                  </div>
                </div>

                <div className="space-y-2">
                  <Label htmlFor="long_description" className="flex items-center gap-2">
                    Long Description <Badge variant="destructive">Required</Badge>
                  </Label>
                  <Textarea
                    id="long_description"
                    value={formData.long_description}
                    onChange={(e) => handleInputChange('long_description', e.target.value)}
                    placeholder="• Intel i7 processor for superior performance&#10;• 16GB RAM for smooth multitasking&#10;• 512GB SSD for fast boot times&#10;• 15.6-inch Full HD display&#10;• Windows 11 operating system"
                    maxLength={10000}
                    rows={8}
                    className={validationErrors.long_description ? 'border-red-500' : ''}
                  />
                  {validationErrors.long_description && (
                    <p className="text-sm text-red-500">{validationErrors.long_description}</p>
                  )}
                  <div className="flex justify-between text-xs text-gray-500">
                    <span>Bullet point format recommended, no external links</span>
                    <span>{formData.long_description.length}/10,000</span>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Media Tab */}
          <TabsContent value="media" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Image className="h-5 w-5" />
                  Product Images
                </CardTitle>
                <CardDescription>
                  Upload and manage product images (max 10 images, 10MB each)
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center">
                  <Image className="h-12 w-12 mx-auto text-gray-400 mb-4" />
                  <p className="text-lg font-medium text-gray-900 mb-2">Upload Product Images</p>
                  <p className="text-gray-500 mb-4">
                    Regular: 500x500px @ 72 PPI | Zoom: 1500x1500px @ 72 PPI
                  </p>
                  <p className="text-sm text-gray-400 mb-4">
                    Supported formats: JPG, PNG, GIF | Max size: 10MB per image
                  </p>
                  <Button variant="outline">
                    <Upload className="h-4 w-4 mr-2" />
                    Choose Images
                  </Button>
                </div>
                
                <div className="mt-4 text-sm text-gray-500">
                  <p>Image Requirements:</p>
                  <ul className="list-disc list-inside mt-2 space-y-1">
                    <li>Direct URLs ending in .jpg, .png, or .gif</li>
                    <li>Publicly accessible without authentication</li>
                    <li>Professional quality with consistent lighting</li>
                    <li>First image serves as primary product representation</li>
                  </ul>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Advanced Tab */}
          <TabsContent value="advanced" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <AlertCircle className="h-5 w-5" />
                  Advanced Settings
                </CardTitle>
                <CardDescription>
                  Pricing, inventory, and additional configuration options
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <div className="space-y-2">
                    <Label htmlFor="price">Price ($)</Label>
                    <Input
                      id="price"
                      value={formData.price}
                      onChange={(e) => handleInputChange('price', e.target.value)}
                      placeholder="999.99"
                      type="number"
                      step="0.01"
                    />
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="msrp">MSRP ($)</Label>
                    <Input
                      id="msrp"
                      value={formData.msrp}
                      onChange={(e) => handleInputChange('msrp', e.target.value)}
                      placeholder="1299.99"
                      type="number"
                      step="0.01"
                    />
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="quantity">Quantity</Label>
                    <Input
                      id="quantity"
                      value={formData.quantity}
                      onChange={(e) => handleInputChange('quantity', e.target.value)}
                      placeholder="10"
                      type="number"
                    />
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="weight">Weight (lbs)</Label>
                    <Input
                      id="weight"
                      value={formData.weight}
                      onChange={(e) => handleInputChange('weight', e.target.value)}
                      placeholder="4.5"
                      type="number"
                      step="0.1"
                    />
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="dimensions">Dimensions (L x W x H)</Label>
                    <Input
                      id="dimensions"
                      value={formData.dimensions}
                      onChange={(e) => handleInputChange('dimensions', e.target.value)}
                      placeholder="14.1 x 9.2 x 0.7 inches"
                    />
                  </div>
                </div>

                <div className="mt-6 p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
                  <h4 className="font-medium text-yellow-800 mb-2">UPC Code Information</h4>
                  <p className="text-sm text-yellow-700">
                    Best Buy requires UPC codes for variants. Clothing UPCs from Mango Spain beginning with 8 or 0 
                    have been tested and resolve without errors in the Best Buy system.
                  </p>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>

        {/* Footer Actions */}
        <div className="mt-8 flex justify-between items-center">
          <div className="flex items-center gap-2 text-sm text-gray-500">
            <CheckCircle2 className="h-4 w-4" />
            Auto-validation enabled
          </div>
          
          <div className="flex gap-4">
            <Button variant="outline" onClick={validateForm} disabled={isLoading}>
              {isLoading ? <Loader2 className="h-4 w-4 animate-spin mr-2" /> : null}
              Validate Form
            </Button>
            <Button onClick={exportTemplate} className="bg-blue-600 hover:bg-blue-700" disabled={isLoading}>
              {isLoading ? <Loader2 className="h-4 w-4 animate-spin mr-2" /> : null}
              Generate Template
            </Button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App

