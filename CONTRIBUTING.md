# Contributing to Best Buy Listing System

Thank you for your interest in contributing to the Best Buy Listing System! This document provides guidelines and information for contributors.

## 🎯 Project Overview

The Best Buy Listing System is a professional marketplace listing management tool that automates the creation of Best Buy-compatible Excel templates. We welcome contributions that improve functionality, documentation, performance, and user experience.

## 🤝 How to Contribute

### Types of Contributions

We welcome several types of contributions:

- **Bug Reports**: Help us identify and fix issues
- **Feature Requests**: Suggest new functionality or improvements
- **Code Contributions**: Submit bug fixes, new features, or optimizations
- **Documentation**: Improve guides, API docs, or code comments
- **Testing**: Add test cases or improve test coverage
- **Performance**: Optimize code for better performance

### Getting Started

1. **Fork the Repository**
   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/bestbuy-listing-system.git
   cd bestbuy-listing-system
   ```

2. **Set Up Development Environment**
   ```bash
   # Run the automated setup
   ./scripts/deploy.sh
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📋 Development Guidelines

### Code Style

#### Python (Backend)
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Maximum line length: 88 characters (Black formatter)

```python
def generate_sku(brand: str, model: str, memory: str, storage: str, condition: str) -> str:
    """
    Generate a standardized SKU for a product.
    
    Args:
        brand: Product brand name
        model: Product model identifier
        memory: Memory configuration (e.g., "32GB")
        storage: Storage configuration (e.g., "1TB")
        condition: Product condition
        
    Returns:
        Formatted SKU string
    """
    # Implementation here
```

#### JavaScript/React (Frontend)
- Use ES6+ features and modern React patterns
- Follow Prettier formatting
- Use meaningful component and variable names
- Implement proper error handling

```javascript
const ProductForm = ({ onSubmit, initialData = {} }) => {
  const [formData, setFormData] = useState(initialData);
  const [errors, setErrors] = useState({});
  
  // Component implementation
};
```

### Commit Messages

Use conventional commit format:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Examples:
```
feat(backend): add Walmart template generation support
fix(frontend): resolve validation error display issue
docs(api): update endpoint documentation for v1.1
```

### Branch Naming

Use descriptive branch names:
- `feature/walmart-integration`
- `fix/validation-error-handling`
- `docs/api-reference-update`
- `refactor/template-generation-optimization`

## 🧪 Testing

### Running Tests

```bash
# Backend tests
cd backend
python -m pytest tests/

# Frontend tests
cd frontend
npm test
```

### Writing Tests

#### Backend Tests
```python
import pytest
from bestbuy_template_generator import BestBuyTemplateGenerator

def test_sku_generation():
    generator = BestBuyTemplateGenerator()
    sku = generator.generate_sku("Dell", "7390", "32GB", "1TB", "Refurbished")
    assert sku == "DL-7390-32-1000-RE"
```

#### Frontend Tests
```javascript
import { render, screen } from '@testing-library/react';
import ProductForm from './ProductForm';

test('renders product form with required fields', () => {
  render(<ProductForm />);
  expect(screen.getByLabelText(/brand/i)).toBeInTheDocument();
  expect(screen.getByLabelText(/model/i)).toBeInTheDocument();
});
```

## 📚 Documentation

### API Documentation

When adding new API endpoints, update `docs/api_reference.md`:

```markdown
#### POST /api/new-endpoint
Description of the endpoint.

**Request Body:**
```json
{
  "field": "value"
}
```

**Response:**
```json
{
  "success": true,
  "data": {}
}
```
```

### Code Documentation

- Add docstrings to all Python functions and classes
- Use JSDoc comments for JavaScript functions
- Update README.md for significant changes
- Include examples in documentation

## 🔍 Pull Request Process

### Before Submitting

1. **Test Your Changes**
   ```bash
   # Run all tests
   ./scripts/test.sh
   ```

2. **Update Documentation**
   - Update relevant documentation files
   - Add or update API documentation
   - Update CHANGELOG.md

3. **Check Code Quality**
   ```bash
   # Python linting
   cd backend
   flake8 .
   black .
   
   # JavaScript linting
   cd frontend
   npm run lint
   ```

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Refactoring

## Testing
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Documentation
- [ ] Documentation updated
- [ ] API documentation updated (if applicable)
- [ ] CHANGELOG.md updated

## Screenshots (if applicable)
Add screenshots for UI changes

## Additional Notes
Any additional information or context
```

### Review Process

1. **Automated Checks**: All CI checks must pass
2. **Code Review**: At least one maintainer review required
3. **Testing**: Manual testing for significant changes
4. **Documentation**: Ensure documentation is updated

## 🐛 Bug Reports

### Before Reporting

1. Check existing issues to avoid duplicates
2. Test with the latest version
3. Gather relevant information

### Bug Report Template

```markdown
**Bug Description**
Clear description of the bug

**Steps to Reproduce**
1. Step one
2. Step two
3. Step three

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: [e.g., Ubuntu 22.04]
- Python Version: [e.g., 3.11.0]
- Node Version: [e.g., 20.0.0]
- Browser: [e.g., Chrome 120]

**Additional Context**
Screenshots, logs, or other relevant information
```

## 💡 Feature Requests

### Feature Request Template

```markdown
**Feature Description**
Clear description of the proposed feature

**Use Case**
Why is this feature needed?

**Proposed Solution**
How should this feature work?

**Alternatives Considered**
Other approaches you've considered

**Additional Context**
Mockups, examples, or other relevant information
```

## 🏗️ Architecture Guidelines

### Backend Architecture

- **Modular Design**: Separate concerns into distinct modules
- **Error Handling**: Comprehensive error handling and logging
- **Validation**: Input validation for all endpoints
- **Performance**: Optimize for speed and memory usage

### Frontend Architecture

- **Component Structure**: Reusable, single-responsibility components
- **State Management**: Use React hooks for state management
- **Error Boundaries**: Implement error boundaries for robustness
- **Accessibility**: Follow WCAG guidelines

### Database Design

- **File-based Storage**: Current implementation uses Excel files
- **Future Database**: Plan for database integration
- **Data Validation**: Ensure data integrity
- **Backup Strategy**: Implement backup and recovery

## 🔒 Security Guidelines

### Security Best Practices

- **Input Validation**: Validate all user inputs
- **File Handling**: Secure file upload and processing
- **Environment Variables**: Use environment variables for sensitive data
- **CORS Configuration**: Proper CORS setup for API access

### Reporting Security Issues

For security vulnerabilities, please email directly rather than creating public issues.

## 📞 Getting Help

### Communication Channels

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Documentation**: Check the `docs/` directory first

### Maintainers

- **ALWAZW** - Project maintainer and primary developer

## 🎉 Recognition

Contributors will be recognized in:
- CHANGELOG.md for significant contributions
- README.md contributors section
- GitHub contributors graph

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to the Best Buy Listing System! Your contributions help make marketplace listing management more efficient and professional for everyone.

