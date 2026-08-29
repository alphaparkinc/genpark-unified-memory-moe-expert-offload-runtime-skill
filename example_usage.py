from client import UnifiedMemoryMoeExpertOffloadRuntimeClient

def main():
    client = UnifiedMemoryMoeExpertOffloadRuntimeClient()
    res = client.execute_offloaded_moe_inference('deepseek-ai/DeepSeek-Coder-V2-236B', 64, 16)
    print('MoE Offload Session: ' + res['offload_session_id'] + ' | ' + res['model'])
    print('Active Experts: ' + str(res['active_routed_experts_count']) + ' | RAM: ' + str(res['cpu_ram_allocated_gb']) + ' GB')
    print('PCIe Prefetch: ' + str(res['pcie_prefetch_bandwidth_gb_sec']) + ' GB/s | Speed: ' + str(res['inference_tok_per_sec']) + ' tok/s')

if __name__ == '__main__':
    main()
