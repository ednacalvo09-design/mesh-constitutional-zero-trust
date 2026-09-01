"""
scripts/main.py - Entrada principal do ecossistema (reconstruído)
Compatível com agents/__init__.py + agents/proposer.py
"""

import sys
from pathlib import Path

# Adiciona raiz do projeto ao PATH
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from agents import Proposal
from agents.proposer import ProposerAgent

def main():
    print("="*60)
    print("  ECOSSISTEMA - EXECUÇÃO PRINCIPAL")
    print("="*60)
    
    proposer = ProposerAgent(agent_id="agent_proposer_01")
    
    # Exemplo de proposta
    result = proposer.propose_action(
        description="validar_fluxo_execucao",
        input_data={"origem": "scripts/main.py", "teste": True},
        context={"area": "3-execucao"}
    )
    
    print("\n[OK] Proposta gerada:")
    for k, v in result.items():
        print(f"  {k}: {v}")
    
    print("\n[INFO] Fluxo pronto para validator / orchestrator")
    
if __name__ == "__main__":
    main()
