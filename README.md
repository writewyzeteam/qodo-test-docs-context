# Qodo Documentation Context Test

## Project Purpose

This repository is designed to test AI code review tools' ability to read and apply repository documentation during code reviews.

## Key Documentation

Our technical decisions and requirements are documented in:

1. **Architecture Decisions**: `/docs/architecture/` - ADRs defining our technical standards
2. **Style Guide**: `/docs/style-guide.md` - Coding patterns and conventions
3. **Security Policy**: `/docs/security/security-policy.md` - Security requirements

## Core Principles

### 1. JWT Authentication (ADR-001)
- ✅ Use JWT tokens in HTTP-only cookies
- ❌ Never use session-based authentication
- See: `/docs/architecture/ADR-001-authentication.md`

### 2. Async/Await Only (Style Guide)
- ✅ Use async/await for all async operations
- ❌ Never use callback-based async patterns
- See: `/docs/style-guide.md`

### 3. Rate Limiting Required (Security Policy)
- ✅ All public endpoints must have rate limiting
- ❌ Never deploy unprotected public endpoints
- See: `/docs/security/security-policy.md`

## Testing This Repo

This repo intentionally contains code that violates the above documentation. AI code review tools should:

1. **Detect violations** of documented standards
2. **Reference specific documentation** (ADR numbers, section names)
3. **Suggest compliant alternatives** based on the documented requirements
4. **Explain why** the violation matters (using context from docs)

## Project Structure
