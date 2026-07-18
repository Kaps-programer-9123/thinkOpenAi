**AI Insurance Advisor** is the strongest choice.

Why?

Because it naturally combines **advisory + operations**. It isn't just answering FAQs—it can recommend products, generate quotes, update policies, and complete transactions. That's exactly where agentic patterns add value.

---

# Product Vision

## AI Insurance Advisor

> **An enterprise-grade, multi-agent AI assistant that helps customers understand, compare, purchase, renew, and manage insurance policies using intelligent workflows, enterprise APIs, and voice or chat interactions.**

Imagine this as the first digital advisor a customer speaks to before reaching a human advisor.

---

# High-Level Architecture

```text
                          Customer

                 Voice / Web Chat / Mobile

                           │
                  WebSocket / REST API

                           │
                    AI Insurance Advisor

──────────────────────────────────────────────────────────

                Supervisor / Planner Agent

                           │
      Determines intent, creates execution plan

──────────────────────────────────────────────────────────

 Policy      Quote      Claims     Renewal     Search
 Agent        Agent      Agent      Agent       Agent

        Customer Agent        Knowledge Agent

──────────────────────────────────────────────────────────

             Tool Calling Framework

 Policy API
 Quote API
 Claims API
 CRM API
 Payment API
 Email API
 Document API
 Web Search

──────────────────────────────────────────────────────────

           Memory + Workflow + Decision Engine

 Conversation Memory
 Customer Memory
 Session State
 Business Rules
 Audit Logs

──────────────────────────────────────────────────────────

                    LLM Layer

 Claude
 GPT
 Bedrock
```

---

# Example User Journey

Customer says:

> "I'm buying a new Tesla. What insurance do you recommend?"

The platform should not answer immediately.

Instead, it plans.

```text
Receive Question

↓

Detect Intent

↓

Need Customer Information?

↓

Ask Follow-up Questions

↓

Gather Answers

↓

Search Available Products

↓

Calculate Premium

↓

Compare Policies

↓

Generate Recommendation

↓

Explain Why

↓

Offer Quote

↓

Purchase

↓

Email Documents
```

This is what makes it an **agent**, not a chatbot.

---

# Main Agents

## 1. Supervisor Agent

Brain of the system.

Responsibilities

* Understand intent
* Decide which agents to invoke
* Manage workflow
* Handle failures
* Maintain execution state

Example

```
User

↓

"I want to insure my Tesla."

↓

Supervisor

↓

Quote Agent
↓

Knowledge Agent
↓

Pricing Agent
↓

Recommendation
```

---

## 2. Customer Agent

Handles customer profile.

Tools

```
Get Customer

Update Customer

Identity Verification

Preferences

Address Validation
```

---

## 3. Quote Agent

Calculates insurance quotes.

Uses

```
Vehicle Details

Customer Age

Driving History

Coverage

Discount Rules
```

Returns

```
Premium

Excess

Coverage

Add-ons
```

---

## 4. Policy Agent

Everything after purchase.

```
Create Policy

Renew

Cancel

Modify

Download Documents
```

---

## 5. Knowledge Agent

Uses RAG.

Answers

```
What is comprehensive insurance?

Does this cover flood damage?

What happens if I miss renewal?
```

---

## 6. Search Agent

For information outside enterprise systems.

Example

```
Current EV regulations

Weather

Government information

Vehicle recall
```

---

# Tool Layer

Agents never call APIs directly.

Everything goes through tools.

```
Quote Tool

↓

Quote API


Policy Tool

↓

Policy System


Payment Tool

↓

Payment Gateway


Email Tool

↓

Notification Service
```

Later these tools can become Lambda functions.

---

# Memory

Not just chat history.

```
Conversation Memory

↓

Current conversation


Customer Memory

↓

Customer profile


Workflow Memory

↓

Quote in progress


Long-Term Memory

↓

Preferences


Audit Memory

↓

Every decision
```

---

# Decision Engine

Business rules remain outside prompts.

Example

```
Customer under 25

↓

Increase premium


Vehicle value > £100k

↓

Manual approval


High risk postcode

↓

Extra validation
```

The LLM shouldn't decide business rules.

---

# Voice Flow

```
Browser

↓

Microphone

↓

Speech-to-Text

↓

Supervisor

↓

Agents

↓

Response

↓

Text-to-Speech

↓

Browser Speaker
```

Exactly the same backend works for text chat.

---

# Technology Stack

## Frontend

```
Next.js

React

TypeScript

Tailwind CSS

WebSocket

WebRTC (voice)
```

---

## Backend

```
Python

FastAPI

Uvicorn

Pydantic

AsyncIO
```

---

## Agent Framework

I would recommend **AWS Strands Agents SDK** (which aligns well with the AWS agent ecosystem) combined with **AWS AgentCore** for deployment and runtime capabilities. If you want explicit workflow graphs for complex orchestration, you can optionally introduce **LangGraph** later, but I would avoid mixing too many frameworks in the first version.

---

## AI Models

```
Amazon Bedrock

Claude

GPT

Llama
```

Switch models using a provider interface.

---

## Memory

```
Redis

SQLite (development)

PostgreSQL

DynamoDB (AWS)
```

---

## Vector Database

```
FAISS (local)

OpenSearch

Aurora PostgreSQL + pgvector

Amazon Knowledge Bases (later)
```

---

## Tool Layer

```
Policy API

Quote API

Customer API

Claims API

Payment API

Document API

Email API

Search API
```

Initially mock these with FastAPI services.

---

## Authentication

```
JWT

OAuth2

Amazon Cognito (future)
```

---

## AWS

```
AWS AgentCore Gateway

Lambda

Bedrock

API Gateway

S3

DynamoDB

CloudWatch

EventBridge
```

---

## Deployment

```
Docker

Docker Compose

GitHub Actions

AWS ECS / EKS
```

---

## Observability

```
Langfuse

OpenTelemetry

CloudWatch

Datadog
```

Track

```
Latency

Tokens

Costs

Tool Calls

Failures

Retries

Agent Decisions
```

---

# Suggested Repository Structure

```
ai-insurance-advisor/

├── frontend/
│   ├── React + Next.js
│   └── Voice UI
│
├── backend/
│   ├── FastAPI
│   ├── WebSocket Server
│   └── Authentication
│
├── agents/
│   ├── supervisor.py
│   ├── quote_agent.py
│   ├── policy_agent.py
│   ├── customer_agent.py
│   ├── knowledge_agent.py
│   └── search_agent.py
│
├── tools/
│   ├── quote_tool.py
│   ├── policy_tool.py
│   ├── payment_tool.py
│   ├── email_tool.py
│   └── search_tool.py
│
├── workflows/
│   ├── quote_workflow.py
│   ├── renewal_workflow.py
│   └── purchase_workflow.py
│
├── memory/
│   ├── conversation.py
│   ├── customer.py
│   └── session.py
│
├── mock_services/
│   ├── policy_api/
│   ├── quote_api/
│   ├── claims_api/
│   └── payment_api/
│
├── prompts/
├── docs/
├── docker-compose.yml
└── README.md
```

## Why this project stands out

Unlike a typical AI chatbot, this demonstrates a complete enterprise architecture: a supervisor agent orchestrates specialist agents, each agent invokes well-defined tools, business rules are separated from LLM reasoning, workflow state is persisted, and the same backend supports both voice and text. Starting with mocked enterprise APIs keeps the project easy to run locally while leaving a clear path to replacing them with AWS AgentCore Gateway, Lambda-backed tools, and Bedrock services in later iterations. That progression itself becomes a strong portfolio story because it mirrors how many organizations evolve AI systems from prototypes into production platforms.
