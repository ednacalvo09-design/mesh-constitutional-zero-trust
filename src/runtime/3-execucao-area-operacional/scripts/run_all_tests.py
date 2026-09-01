"""
scripts/run_all_tests.py - BATERIA DE TESTES (versão corrigida)
Valida agents/__init__.py e agents/proposer.py
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from agents import BaseAgent, Proposal
from agents.proposer import ProposerAgent

class TestAgentsStructure(unittest.TestCase):
    def test_base_agent_import(self):
        self.assertTrue(issubclass(ProposerAgent, BaseAgent))
    
    def test_proposal_has_trace_id(self):
        p = Proposal(action="test")
        self.assertTrue(len(p.trace_id) == 8)
        self.assertEqual(p.status, "proposed")
    
    def test_proposer_returns_dict(self):
        proposer = ProposerAgent()
        result = proposer.propose_action("testar_integracao")
        self.assertIn("trace_id", result)
        self.assertIn("action", result)
        self.assertIn("output_data", result)
        self.assertEqual(result["action"], "testar_integracao")
    
    def test_proposer_execute(self):
        proposer = ProposerAgent()
        prop = Proposal(action="exec_test")
        out = proposer.execute(prop)
        self.assertEqual(out.status, "proposed")

def run_suite():
    print("="*60)
    print("  MESH - BATERIA GLOBAL DE TESTES DE ARQUITETURA")
    print("="*60)
    
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestAgentsStructure)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "="*60)
    if result.wasSuccessful():
        print("  🎉 TODOS OS TESTES APROVADOS COM SUCESSO! 🎉")
    else:
        print("  ❌ FALHAS ENCONTRADAS")
    print("="*60)
    
    return 0 if result.wasSuccessful() else 1

if __name__ == "__main__":
    sys.exit(run_suite())
