import json
from rank_bm25 import BM25Okapi

class SupportAgent:
    def __init__(self, knowledge_base_path):
        with open(knowledge_base_path, 'r') as f:
            self.knowledge_base = json.load(f)
        
        self.questions = [item["question"] for item in self.knowledge_base["questions"]]
        tokenized_questions = [q.lower().split() for q in self.questions]
        self.bm25 = BM25Okapi(tokenized_questions)
    
    def calculate_tag_score(self, user_input, tags):
        """Calculate bonus score based on tag matches."""
        user_tokens = set(user_input.lower().split())
        tag_tokens = set([tag.lower() for tag in tags])
        matches = user_tokens.intersection(tag_tokens)
        return len(matches) * 3.0
    
    def find_answer(self, user_input):
        """Find best answer using BM25 + tag matching."""
        tokenized_query = user_input.lower().split()
        bm25_scores = self.bm25.get_scores(tokenized_query)
        
        # Add tag bonus to scores
        final_scores = []
        for idx, item in enumerate(self.knowledge_base["questions"]):
            tag_bonus = self.calculate_tag_score(user_input, item.get("tags", []))
            final_score = bm25_scores[idx] + tag_bonus
            final_scores.append(final_score)
        
        best_index = max(range(len(final_scores)), key=lambda i: final_scores[i])
        best_score = final_scores[best_index]
        
        # Threshold for relevance
        if best_score > 1.0:
            return self.knowledge_base["questions"][best_index]["answer"]
        return None
    
    def get_response(self, user_input):
        """Get response for user input."""
        answer = self.find_answer(user_input)
        
        if answer:
            return answer
        
        user_lower = user_input.lower()
        
        if any(word in user_lower for word in ["hello", "hi", "hey"]):
            return "Hello! I'm here to help answer questions about Thoughtful AI. How can I assist you today?"
        elif any(word in user_lower for word in ["thank", "thanks"]):
            return "You're welcome! Let me know if you have any other questions."
        else:
            return "I'm trained to answer questions about Thoughtful AI's agents like EVA, CAM, and PHIL. Could you rephrase your question about our automation agents?"
