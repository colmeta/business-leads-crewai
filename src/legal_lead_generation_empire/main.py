#!/usr/bin/env python
"""
Legal Lead Generation Empire - Main Execution File

This is your command center for running the PI lawyer lead generation business.
Based on the 3-phase blueprint: Manual → Automated → Scale
"""
import sys
from legal_lead_generation_empire.crew import LegalLeadGenerationEmpireCrew

def run():
    """
    Run the full crew - This executes your entire lead generation operation.
    
    Use this for daily operations once you have partner firms and active ad campaigns.
    """
    print("\n" + "="*60)
    print("🚀 LEGAL LEAD GENERATION EMPIRE - FULL RUN")
    print("="*60 + "\n")
    
    # These inputs control your entire operation
    inputs = {
        # TARGET MARKET
        'target_city': 'Los Angeles',  # Start here, then expand to Miami, Houston, etc.
        'research_depth': 'deep',  # 'quick' for 10 firms, 'deep' for 30 firms
        
        # LEAD GENERATION
        'daily_ad_budget': 50,  # Start with $50/day, scale to $200+ as you prove ROI
        'lead_score_threshold': 7,  # Only pass leads scoring 7+ to attorneys
        
        # OUTREACH
        'target_firms': 20,  # Number of firms to contact in this batch
        'outreach_batch_size': 5,  # Contact 5 firms per day (manageable follow-up)
        'follow_up_cadence': 'aggressive',  # 'gentle' or 'aggressive'
        
        # OPERATIONS
        'daily_qualified_leads': 'from_source_task',  # Pulls from lead qualification task
        'partner_firms': 'from_network_task',  # Pulls from network building task
        'pricing_model': 'pay_per_show',  # $1,000 per consultation show-up
    }
    
    print(f"📍 Target Market: {inputs['target_city']}")
    print(f"💰 Daily Ad Budget: ${inputs['daily_ad_budget']}")
    print(f"🎯 Lead Threshold: {inputs['lead_score_threshold']}/10")
    print(f"📧 Outreach Target: {inputs['target_firms']} firms")
    print(f"💵 Pricing: {inputs['pricing_model']} ($1,000/show)")
    print("\n" + "-"*60 + "\n")
    
    # Kickoff the crew
    result = LegalLeadGenerationEmpireCrew().crew().kickoff(inputs=inputs)
    
    print("\n" + "="*60)
    print("✅ CREW EXECUTION COMPLETE")
    print("="*60 + "\n")
    
    return result


def run_phase_1_research():
    """
    Phase 1: Market Research Only
    
    Use this for your first run to identify target law firms in your city.
    This will give you the 20-30 firms to contact with your risk-free offer.
    """
    print("\n" + "="*60)
    print("🔍 PHASE 1: MARKET RESEARCH - Finding Target Law Firms")
    print("="*60 + "\n")
    
    inputs = {
        'target_city': 'Los Angeles',
        'research_depth': 'deep',
        'service_categories': 'Personal Injury Law',
        'service_types': 'Car Accidents, Slip and Fall, Motorcycle Injuries',
        'target_businesses': 'to_be_determined',
        'pricing_model': 'pay_per_show',
        'daily_leads': 'not_started_yet',
        'provider_network': 'not_started_yet',
        'daily_ad_budget': 0,
        'lead_score_threshold': 7,
        'outreach_batch_size': 5,
        'follow_up_cadence': 'aggressive'
    }
    
    # Only run the first task (research)
    crew = LegalLeadGenerationEmpireCrew().crew()
    # Note: You'll need to modify crew.py to support running individual tasks
    # For now, this will run all tasks, but you can comment out tasks 2-4 in crew.py
    
    result = crew.kickoff(inputs=inputs)
    
    print("\n📊 Research Complete! Check your output for the target firm list.")
    print("Next step: Run 'run_phase_1_outreach' to contact these firms.\n")
    
    return result


def run_phase_1_outreach():
    """
    Phase 1: Outreach Campaign
    
    Use this after research to contact your target firms with the risk-free offer.
    """
    print("\n" + "="*60)
    print("📧 PHASE 1: OUTREACH - Contacting Law Firms")
    print("="*60 + "\n")
    
    # You would load the research results here
    inputs = {
        'target_city': 'Los Angeles',
        'target_firms': 20,
        'outreach_batch_size': 5,
        'follow_up_cadence': 'aggressive',
        'pricing_model': 'pay_per_show',
        'research_depth': 'completed',
        'service_categories': 'Personal Injury Law',
        'service_types': 'Car Accidents, Slip and Fall, Motorcycle Injuries',
        'target_businesses': 'from_research_results',
        'daily_leads': 'not_started_yet',
        'provider_network': 'building',
        'daily_ad_budget': 0,
        'lead_score_threshold': 7
    }
    
    result = LegalLeadGenerationEmpireCrew().crew().kickoff(inputs=inputs)
    
    print("\n✉️ Outreach Complete! Follow up with firms that responded.")
    print("Next step: Once you have 1 firm, run 'run_phase_1_lead_gen' to start delivering.\n")
    
    return result


def run_phase_1_lead_gen():
    """
    Phase 1: Manual Lead Generation & Matching
    
    Use this when you have your first partner firm. This runs the lead sourcing
    and matching operations to prove the model works.
    """
    print("\n" + "="*60)
    print("🎯 PHASE 1: LEAD GENERATION - Delivering for First Client")
    print("="*60 + "\n")
    
    inputs = {
        'target_city': 'Los Angeles',
        'daily_ad_budget': 50,  # Start with $50/day
        'lead_score_threshold': 7,
        'daily_qualified_leads': 'from_ad_campaigns',
        'partner_firms': '1_test_firm',  # Your first client
        'pricing_model': 'pay_per_show',
        'research_depth': 'completed',
        'service_categories': 'Personal Injury Law',
        'service_types': 'Car Accidents, Slip and Fall, Motorcycle Injuries',
        'target_businesses': 'completed',
        'provider_network': '1_active_firm',
        'target_firms': 0,
        'outreach_batch_size': 0,
        'follow_up_cadence': 'none'
    }
    
    result = LegalLeadGenerationEmpireCrew().crew().kickoff(inputs=inputs)
    
    print("\n🎉 Lead generation active! Monitor your daily matching operations.")
    print("Goal: Deliver 2-3 qualified leads in 30 days to prove the model.\n")
    
    return result


def train():
    """
    Train the crew to optimize performance.
    
    Use this after you have real data to improve the agents' decision-making.
    """
    inputs = {
        'target_city': 'Los Angeles',
        'service_categories': 'Personal Injury Law',
        'service_types': 'Car Accidents, Slip and Fall, Motorcycle Injuries',
        'target_businesses': 'sample_data',
        'pricing_model': 'pay_per_show',
        'daily_leads': 'sample_data',
        'provider_network': 'sample_data',
        'research_depth': 'deep',
        'daily_ad_budget': 50,
        'lead_score_threshold': 7,
        'outreach_batch_size': 5,
