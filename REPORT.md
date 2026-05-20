# **PromoCatch Project Report**
## Campaign and Deal Tracking System

### **Executive Summary**

PromoCatch is a campaign and deal tracking system developed as a Software Architecture course project. It consists of two phases demonstrating the evolution from initial architectural design (Phase 1) to complete implementation with full features (Phase 2). The system follows a strict layered REST API architecture and helps users browse, search, create, update, and manage retail and financial promotions from platforms like Zubizu and Bonus Flash.

---

### **1. Project Overview**

**Project Name:** PromoCatch - Campaign and Deal Tracking System

**Purpose:** To collect campaign and promotion information in a centralized, user-friendly web application

**Phases:**
- **Phase 1** (Deadline: 04.05.2026): Architecture design and initial implementation
- **Phase 2** (Deadline: 24.05.2026): Complete implementation with full features and documentation

**Repository Structure:**
- `/phase1/`: Initial implementation with SAD V1
- `/phase2/`: Final version with complete features, SAD V2, and deployment resources

---

### **2. Architectural Design**

#### **2.1 Architecture Style: Layered Architecture**

The system implements a strict four-layer architecture:

1. **Presentation Layer** - User Interface
   - File: `static/index.html`
   - Technology: HTML, CSS, Bootstrap, Vanilla JavaScript
   - Responsibility: Display campaign cards, handle user input, send HTTP requests

2. **Control Layer** - Request Handling & Routing
   - Files: `main.py`, `routers.py`
   - Technology: FastAPI
   - Responsibility: Define REST endpoints, validate HTTP requests, orchestrate business logic

3. **Domain Layer** - Business Logic & Validation
   - Files: `schemas.py`, `services.py`
   - Technology: Pydantic, Python
   - Responsibility: Enforce business rules, normalize data, coordinate service operations

4. **Resource Layer** - Data Persistence
   - Files: `database.py`, `models.py`, `repository.py`
   - Technology: SQLAlchemy, SQLite
   - Responsibility: Database operations, ORM mapping, persistent storage

**Data Flow:**
```
User Interface → FastAPI Router → Service Layer → Repository Layer → SQLite Database
```

#### **2.2 Core Domain Model**

**Campaign Entity:**
- `id` (Integer, Primary Key, Indexed)
- `title` (String, 3-120 chars, Required, Indexed)
- `platform` (String, 2-80 chars, Required, Indexed)
- `description` (Text, Min 10 chars, Required)
- `discount_rate` (Integer, 1-100%, Required)

**Validation Rules:**
- Title: minimum 3 characters, maximum 120
- Platform: minimum 2 characters, maximum 80
- Description: minimum 10 characters
- Discount Rate: range 1-100%

---

### **3. Technology Stack**

| Layer | Technologies |
|-------|--------------|
| **Backend** | Python 3.11+, FastAPI, SQLAlchemy |
| **Database** | SQLite (persistent file-based database) |
| **Frontend** | HTML5, CSS3, Bootstrap 5.3.3, Vanilla JavaScript |
| **Deployment** | Docker, Docker Compose, Uvicorn |

**Key Dependencies:**
- `fastapi`: Web framework
- `uvicorn[standard]`: ASGI server
- `sqlalchemy`: ORM framework

---

### **4. API Endpoints & Functionality**

#### **4.1 RESTful API**

| Method | Endpoint | Phase 1 | Phase 2 | Description |
|--------|----------|---------|---------|-------------|
| GET | `/campaigns` | ✓ | ✓ | List campaigns with optional filters |
| GET | `/campaigns/{campaign_id}` | ✓ | ✓ | Retrieve single campaign |
| POST | `/campaigns` | ✓ | ✓ | Create new campaign |
| PUT | `/campaigns/{campaign_id}` | ✓ | ✓ | Update existing campaign |
| DELETE | `/campaigns/{campaign_id}` | ✗ | ✓ | Delete campaign |
| GET | `/health` | ✓ | ✗ | System health check |

#### **4.2 Query Parameters**

The GET `/campaigns` endpoint supports advanced filtering:

- **`q`** (Optional): Full-text search in campaign title and description
- **`platform`** (Optional): Filter by platform name (case-insensitive)
- **`min_discount`** (Optional): Minimum discount rate (1-100)
- **`max_discount`** (Optional): Maximum discount rate (1-100)

**Example:** 
```
GET /campaigns?q=coffee&platform=coffee&min_discount=20&max_discount=50
```

---

### **5. Phase 1 Analysis**

#### **5.1 Scope & Deliverables**

**Objectives:**
- System selection and requirements definition
- Architectural design (SAD V1)
- Initial implementation of core functionality
- Database setup with SQLite

**Deliverables:**
- System Architecture Document (SAD V1)
- Core backend implementation (4 layers)
- Partial frontend UI
- Use case, logical, and process views documentation
- Docker deployment configuration

#### **5.2 Implemented Use Cases**

1. **View Active Campaigns**: Users can retrieve and display all campaigns from the database
2. **Add New Campaign**: Users can submit a form to create new campaign records

#### **5.3 Frontend Implementation**

- Display active campaigns as cards
- Form for adding new campaigns
- Bootstrap-based responsive design
- Vanilla JavaScript for API communication using Fetch API

#### **5.4 Key Features**

- Data persistence with SQLite
- RESTful API with automatic documentation (Swagger UI at `/docs`)
- Input validation at multiple layers (Pydantic schemas, repository level)
- Seed data: 4 sample campaigns preloaded on startup
- Docker containerization for easy deployment

#### **5.5 Seeding Strategy**

Phase 1 includes automatic data seeding with sample campaigns:
- Spring Fashion Sale (StyleHub, 20% discount)
- Grocery Cashback Weekend (Bonus Plus, 15% discount)
- Coffee Club Weekday Offer (Coffee Club, 30% discount)
- Official Merchandise Giveaway (Fan Store, 100% discount)

**Note:** Phase 1 also includes legacy campaign fixes handling for Turkish character encoding issues.

---

### **6. Phase 2 Analysis**

#### **6.1 Evolution from Phase 1**

Phase 2 extends Phase 1 with complete functionality and comprehensive documentation. Key additions:

**New Features:**
- Delete campaign functionality (`DELETE` endpoint)
- Advanced search and filtering UI
- Campaign editing interface
- Campaign detail view
- Full-featured frontend with enhanced UX

**Enhanced Documentation:**
- Extended SAD V2 with all architectural views
- Process view with sequence diagrams
- Screenshots of application interfaces
- Presentation files for technical overview

#### **6.2 Complete Use Case Implementation**

Phase 2 implements all seven core use cases:

1. **View Campaign List** - Display all campaigns with pagination/scrolling
2. **Search Campaigns** - Full-text search across title and description
3. **Filter by Platform/Discount** - Multi-criteria filtering
4. **Create Campaign** - Submit form to add new campaign
5. **Update Campaign** - Edit existing campaign details
6. **Delete Campaign** - Remove campaigns from database
7. **View Campaign Detail** - Display individual campaign information

#### **6.3 Frontend Enhancements**

- Complete CRUD interface
- Advanced search and filter UI components
- Edit/delete campaign modals
- Form validation and error handling
- Bootstrap 5 styling with custom color scheme
- Responsive design for multiple screen sizes
- Professional typography and spacing

**UI Color Scheme:**
- Navy: #0f172a (primary)
- Navy soft: #1e293b (secondary)
- Accent: #38bdf8 (sky blue)
- Success: #16a34a (green)

#### **6.4 Deployment Options**

**Windows Users:**
- `run_local.bat` - Simple batch script execution
- `run_local.ps1` - PowerShell script with venv setup

**Unix/Mac/General:**
- Manual command: `python -m uvicorn main:app --reload`
- Docker Compose: `docker compose up --build`

**Access URLs (Phase 2 local):**
- Frontend UI: `http://127.0.0.1:8010` (batch/PowerShell)
- Swagger API Docs: `http://127.0.0.1:8010/docs`
- Default uvicorn: `http://127.0.0.1:8000`

#### **6.5 Documentation Quality**

Phase 2 includes:
- Complete SAD V2 document with all architectural views
- Use case diagrams with all 7 use cases
- Component diagrams showing layer interactions
- Sequence diagrams for key workflows
- Domain model diagrams
- 3 screenshots documenting UI and API explorer
- Detailed README with multiple run options

---

### **7. Implementation Quality Analysis**

#### **7.1 Code Organization**

**Strengths:**
- Clear separation of concerns across layers
- Type hints throughout codebase (Python type annotations)
- Pydantic schema validation
- SQLAlchemy ORM abstraction
- Consistent naming conventions
- Well-documented endpoint descriptions

**Files & Responsibilities:**

| File | Lines | Responsibility |
|------|-------|-----------------|
| `main.py` | ~50 | FastAPI app setup, lifespan, routes mounting |
| `routers.py` | ~95 | HTTP endpoint definitions, request/response mapping |
| `services.py` | ~70-120 | Business logic, data normalization, validation |
| `repository.py` | ~90 | Database operations, query building |
| `models.py` | ~15 | SQLAlchemy ORM model definition |
| `schemas.py` | ~30 | Pydantic validation schemas |
| `database.py` | ~20 | Database configuration, session management |

#### **7.2 Error Handling**

- HTTP status codes (201 for create, 404 for not found, 204 for delete)
- HTTPException with descriptive messages
- Data validation at schema level
- Query parameter validation (min_length, ge, le)

#### **7.3 Performance Considerations**

- Database indexing on frequently queried fields (id, title, platform)
- Order by id descending (latest campaigns first)
- Case-insensitive search using LIKE queries
- SQLAlchemy automatic connection pooling

---

### **8. Key Differences Between Phases**

| Feature | Phase 1 | Phase 2 |
|---------|---------|---------|
| **Use Cases** | 2 (View, Add) | 7 (Full CRUD + Search/Filter) |
| **API Endpoints** | 4 | 5 (+ health check in Phase 1) |
| **Delete Feature** | ✗ | ✓ |
| **Edit Feature** | ✗ | ✓ |
| **Frontend** | Partial UI | Complete interface |
| **Documentation** | SAD V1 | SAD V1 + SAD V2 |
| **Screenshots** | None | 3 detailed UI screenshots |
| **Windows Runners** | None | `run_local.bat`, `run_local.ps1` |
| **Deployment Info** | Basic Docker | Full Docker + PowerShell support |
| **Presentation Files** | None | Build scripts for presentation PDFs |

---

### **9. Database Schema**

**Table: campaigns**

```sql
CREATE TABLE campaigns (
    id INTEGER PRIMARY KEY,
    title VARCHAR(120) NOT NULL,
    platform VARCHAR(80) NOT NULL,
    description TEXT NOT NULL,
    discount_rate INTEGER NOT NULL
);

CREATE INDEX idx_campaigns_id ON campaigns(id);
CREATE INDEX idx_campaigns_title ON campaigns(title);
CREATE INDEX idx_campaigns_platform ON campaigns(platform);
```

**Sample Data:**
- Spring Fashion Sale: StyleHub, 20% discount
- Grocery Cashback Weekend: Bonus Plus, 15% discount  
- Coffee Club Weekday Offer: Coffee Club, 30% discount
- Official Merchandise Giveaway: Fan Store, 100% discount

---

### **10. Development & Deployment**

#### **10.1 Prerequisites**

- Python 3.11 or newer
- pip (Python package manager)
- (Optional) Docker and Docker Compose for containerized deployment

#### **10.2 Installation Steps (Phase 2)**

**Option A - Local Direct Execution:**
```bash
cd phase2
pip install -r requirements.txt
python -m uvicorn main:app --reload
# Access at http://127.0.0.1:8000
```

**Option B - Windows Batch Script:**
```bash
cd phase2
./run_local.bat
# Access at http://127.0.0.1:8010
```

**Option C - Docker Compose:**
```bash
cd phase2
docker compose up --build
# Access at http://127.0.0.1:8000
```

#### **10.3 Testing & Validation**

- Swagger UI: `/docs` endpoint for interactive API testing
- Sample data automatically seeded on first run
- Manual testing of all CRUD operations possible through UI

---

### **11. Architectural Strengths**

1. **Clear Separation of Concerns**: Each layer has well-defined responsibilities
2. **Scalability**: Layered design allows independent modification of layers
3. **Testability**: Components can be tested in isolation
4. **Maintainability**: Clear structure makes code easy to understand and modify
5. **Validation**: Multi-level validation (schema + repository)
6. **Documentation**: Comprehensive architectural documentation with diagrams
7. **Modern Stack**: Uses current, well-supported frameworks (FastAPI, SQLAlchemy)
8. **Type Safety**: Python type hints improve code reliability
9. **API Discoverability**: Auto-generated Swagger documentation

---

### **12. Potential Improvements & Future Scope**

1. **Authentication & Authorization**: User roles and permissions
2. **Database**: Migration to PostgreSQL for production scalability
3. **Caching**: Redis for frequently accessed campaigns
4. **Search**: Full-text search implementation (Elasticsearch)
5. **Notifications**: Alert users about new campaigns
6. **Analytics**: Campaign performance tracking and statistics
7. **Testing**: Unit and integration test suite
8. **API Versioning**: Support for API v2 with backward compatibility
9. **Rate Limiting**: API rate limiting for protection
10. **Logging**: Structured logging for debugging and monitoring

---

### **13. Project Statistics**

**Code Distribution:**
- Python Backend: ~400 lines of code
- Frontend (HTML/CSS/JS): ~200+ lines
- Documentation: SAD V1 + SAD V2, README files
- Configuration: Docker files, requirements.txt

**Layers Count:**
- Presentation Layer: 1 file (index.html)
- Control Layer: 2 files (main.py, routers.py)
- Domain Layer: 2 files (schemas.py, services.py)
- Resource Layer: 3 files (database.py, models.py, repository.py)

**API Endpoints:** 5 total (8 methods across different paths)

---

### **14. Conclusion**

PromoCatch demonstrates a well-structured, educational implementation of layered architecture principles applied to a real-world use case. The project successfully evolves from Phase 1's foundational design to Phase 2's complete implementation, showing careful attention to:

- **Architecture**: Clean layered design with clear separation
- **Implementation**: Professional code organization and type safety
- **Documentation**: Comprehensive SAD with architectural views
- **User Experience**: Full-featured frontend with advanced capabilities
- **Deployment**: Multiple options for local and containerized execution

The project serves as an excellent reference for learning software architecture patterns and RESTful API design. Phase 2 represents a production-ready feature set with proper documentation, error handling, and deployment infrastructure.

---

