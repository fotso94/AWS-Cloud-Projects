#!/usr/bin/env python3
"""
Test script for AWS Translate functionality
Tests multiple language combinations and provides feedback
"""

import boto3
import os
import sys

def test_translation(source_lang, target_lang, test_text):
    """Test translation for a specific language pair"""
    print(f"\n🔄 Testing {source_lang} → {target_lang}")
    print(f"Original: {test_text}")
    
    try:
        translate = boto3.client('translate')
        
        result = translate.translate_text(
            Text=test_text,
            SourceLanguageCode=source_lang,
            TargetLanguageCode=target_lang
        )
        
        translated_text = result['TranslatedText']
        print(f"✅ Translated: {translated_text}")
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def main():
    """Run translation tests"""
    print("🌍 AWS Translate Language Testing Tool")
    print("=" * 50)
    
    # Test text samples
    test_phrases = [
        "Hello, welcome to our website!",
        "Contact us for more information",
        "Tech Conferences",
        "About me"
    ]
    
    # Language combinations to test
    language_pairs = [
        ("en", "es"),  # English to Spanish
        ("en", "fr"),  # English to French
        ("en", "de"),  # English to German
        ("en", "pt"),  # English to Portuguese
        ("en", "it"),  # English to Italian
    ]
    
    success_count = 0
    total_tests = 0
    
    for phrase in test_phrases:
        print(f"\n📝 Testing phrase: '{phrase}'")
        print("-" * 40)
        
        for source, target in language_pairs:
            total_tests += 1
            if test_translation(source, target, phrase):
                success_count += 1
    
    print(f"\n📊 Test Results:")
    print(f"✅ Successful: {success_count}/{total_tests}")
    print(f"❌ Failed: {total_tests - success_count}/{total_tests}")
    
    if success_count == total_tests:
        print("🎉 All tests passed! AWS Translate is working correctly.")
    else:
        print("⚠️  Some tests failed. Check your AWS credentials and permissions.")

if __name__ == "__main__":
    main()
